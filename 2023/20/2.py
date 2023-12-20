from collections import defaultdict
from enum import Enum
import json
import os, sys
import time

class ModuleType(Enum):
    FLIPFLOP = "%"
    CONJUCTION = "&"
    BROADCAST = "#"
    OUTPUT = "+"

class Module:
    def __init__(self, name: str, modType: ModuleType, connected: list[str]):
        self.name = name
        self.connected_names = connected
        self.connected: list["Module"] = []
        self.input_modules: dict[str, bool] = {}
        self.modType = modType
        self.initial_state = False
    
    def init(self, modules: dict[str, "Module"]):
        self.connected = []
        for name in self.connected_names:
            if name not in modules:
               self.connected.append(Module(name, ModuleType.OUTPUT, []))
            else:
                self.connected.append(modules[name])
                modules[name].input_modules[self.name] = False
    
    def process(self, name: str, pulse: bool) -> list[tuple[str, bool]]:
        affected: list[tuple[str, bool]] = []
        if self.modType == ModuleType.FLIPFLOP:
            if pulse == False:
                self.initial_state = not self.initial_state
                for module in self.connected:
                    affected.append((module.name, self.initial_state))
        elif self.modType == ModuleType.BROADCAST:
            for module in self.connected:
                affected.append((module.name, pulse))
        elif self.modType == ModuleType.CONJUCTION:
            self.input_modules[name] = pulse
            is_all_high = True
            for saved_pulse in self.input_modules.values():
                if not saved_pulse:
                    is_all_high = False
                    break
            if is_all_high:
                for module in self.connected:
                    affected.append((module.name, False))
            else:
                for module in self.connected:
                    affected.append((module.name, True))
        elif self.modType == ModuleType.OUTPUT:
            pass
        return affected
    def __repr__(self) -> str:
        return f"{self.name} {self.modType} {self.connected_names}"

def dump_to_json(modules: dict[str, Module]):
    # a json dump to see the structure of the modules
    # from the rx modules point of view
    # all reversed, so input modules are children of the output modules
    
    # this is a dictionary, that will build up the json
    module_references = {
        "rx+": {}
    }
    # the final json dictionary to be written
    json_modules = {"rx+": module_references["rx+"]}
    # already seen modules will not be inserted to prevent cycles
    seen = set()
    # create a queue of all modules connected to rx
    queue = [("rx", [key for key, _ in modules["rx"].input_modules.items()])]
    while(queue):
        # pop the first element
        name, connected = queue.pop(0)
        # and skip if already added somewhere else
        if name in seen:
            continue
        seen.add(name)
        # get the name with the type
        name_with_type = name + str(modules[name].modType.value)
        # for each module that is connected
        for module in connected:
            # if not already seend and actually is a module
            if module not in seen and module in modules:
                # add it and its connected modules to the queue
                queue.append((module, [key for key, _ in modules[module].input_modules.items()]))
            # also update the dictionary
            if module in modules:
                # get the module type
                module_with_type = module + str(modules[module].modType.value)
                # initialize an empty object at that position
                module_references[name_with_type][module_with_type] = {}
                # and add it also as a high level object to the dictionary
                module_references[module_with_type] = module_references[name_with_type][module_with_type]
    with open(os.path.join(sys.path[0],"input.json"), "w", encoding="utf-8") as f:
        json.dump(json_modules, f, indent=2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    modules: dict[str, Module] = {}
    # read in input
    broadcaster = None
    for line in lines:
        name = ""
        moduleType = None
        if line.startswith("%"):
            name = line[1:].split(" -> ")[0]
            moduleType = ModuleType.FLIPFLOP
        elif line.startswith("&"):
            name = line[1:].split(" -> ")[0]
            moduleType = ModuleType.CONJUCTION
        else:
            name = "broadcaster"
            moduleType = ModuleType.BROADCAST
        connected = line.split(" -> ")[1].split(", ")
        modules[name] = Module(name, moduleType, connected)
    # add missing rx module
    modules["rx"] = Module("rx", ModuleType.OUTPUT, [])
    # initialize all modules
    for module in modules.values():
        module.init(modules)
    broadcaster = modules["broadcaster"]
    
    
    # after analyzing the input
    # the parents of rx are NAND gates, which only have NAND gates as parents
    # therefore we can simplify the problem to finding the cycle length of each NAND gate
    # first retrieve parents from RX
    rx_input = [modules[key] for key in modules["rx"].input_modules.keys()]
    
    # get Parents from Parents
    rx_input_inputs: list[list[Module]] = []
    for mod in rx_input:
        rx_input_inputs.append([modules[key] for key in mod.input_modules.keys()])
    
    # a cycle counter for each Grandparent
    cycle_counters = defaultdict(int)
    # as long as all Grandparents of any parent of rx are not high
    # we run the program
    run_program = True
    # index to the Parent that will send out the pulse
    output_index = 0
    # a counter on how many times the button was pressed
    button_counter = 0
    
    while(run_program):
        # we press the button
        button_counter += 1
        affected = broadcaster.process("button", False)
        # and propagate
        queue: list[tuple[str, str, bool]] = [("broadcaster", name, pulse) for name, pulse in affected]
        while queue:
            src, module, pulse = queue.pop(0)
            # the rx module is an output module, so we skip it
            if module == "rx":
                continue
            affected = modules[module].process(src, pulse)
            # if the rx module is connected to this NAND Gate, this is a Parent
            if "rx" in modules[module].connected_names:
                # for each Parent of the Parent
                for name, pulse in modules[module].input_modules.items():
                    # if the last pulse to this Parent from this Grandparent was a high pulse
                    # and this did not happen before
                    # we found a cycle for that Grandparent
                    if pulse and cycle_counters[name] == 0:
                        cycle_counters[name] = button_counter
            queue.extend([(module, name, pulse) for name, pulse in affected])
        
        # for all Parents of rx
        for i, mods in enumerate(rx_input_inputs):
            # if we found a cycle for all Parents of that Parent
            if all([cycle_counters[mod.name] != 0 for mod in mods]):
                # we found the Parent that will send out the pulse
                # and can stop the program
                output_index = i
                run_program = False
                break
    # the cycles we are interested in are the cycles of the Parents of the Parent of RX that sends out the pulse
    cycles = [cycle_counters[mod.name] for mod in rx_input_inputs[output_index]]
    # we calculate the lcm of all cycles
    current_lcm = 1
    for cycle_length in cycles:
        current_lcm = lcm(current_lcm, cycle_length)
    print(current_lcm)
        
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
