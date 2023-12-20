from enum import Enum
import os, sys
import time

class ModuleType(Enum):
    FLIPFLOP = 0
    CONJUCTION = 1
    BROADCAST = 2
    OUTPUT = 3

class Module:
    def __init__(self, name: str, modType: ModuleType, connected: list[str]):
        # the name of the module
        self.name = name
        # the names of the modules this module is connected to for later initialization
        self.connected_names = connected
        # the module objects this module is connected to
        self.connected: list["Module"] = []
        # the input modules and their current state
        self.input_modules: dict[str, bool] = {}
        # the type of the module
        self.modType = modType
        # the initial state of the module
        self.initial_state = False
    
    def init(self, modules: dict[str, "Module"]):
        self.connected = []
        # for each connected name
        for name in self.connected_names:
            # if the naem is not in the modules, it is an output module
            if name not in modules:
               self.connected.append(Module(name, ModuleType.OUTPUT, []))
            # otherwise set the connected module object
            else:
                self.connected.append(modules[name])
                # and set the input module state to False
                modules[name].input_modules[self.name] = False
    
    def process(self, name: str, pulse: bool) -> tuple[int, int, list[tuple[str, bool]]]:
        # counter for how many lows and highs are sent
        low, high = 0, 0
        # list of modules and the state they get sent
        affected: list[tuple[str, bool]] = []
        # if this is a flipflop
        if self.modType == ModuleType.FLIPFLOP:
            # if the pulse is False, we need to flip the state
            if pulse == False:
                self.initial_state = not self.initial_state
                # and send the flipped state as a pulse
                for module in self.connected:
                    affected.append((module.name, self.initial_state))
                # update counters
                if self.initial_state:
                    high = len(self.connected)
                else:
                    low = len(self.connected)
        # if this is a broadcaster
        elif self.modType == ModuleType.BROADCAST:
            # we broadcast the pulse to all connected modules
            for module in self.connected:
                affected.append((module.name, pulse))
            # update counters
            if pulse:
                high = len(self.connected)
            else:
                low = len(self.connected)
        # if this is a NAND gate
        elif self.modType == ModuleType.CONJUCTION:
            # we save the pulse to the input modules
            self.input_modules[name] = pulse
            # check if all ar high
            is_all_high = True
            for saved_pulse in self.input_modules.values():
                if not saved_pulse:
                    is_all_high = False
                    break
            # and send low pulse if all are high
            # update counters
            if is_all_high:
                for module in self.connected:
                    affected.append((module.name, False))
                low = len(self.connected)
            else:
                for module in self.connected:
                    affected.append((module.name, True))
                high = len(self.connected)
        # output modules eat pulses
        elif self.modType == ModuleType.OUTPUT:
            pass
        # return the counters and the affected modules
        return low, high, affected
    def __repr__(self) -> str:
        return f"{self.name} {self.modType} {self.connected_names}"

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
    # after setting all connected names
    # we update the object lists and input modules
    for module in modules.values():
        module.init(modules)
    
    broadcaster = modules["broadcaster"]
    
    total_low, total_high = 0, 0
    # for all button presses
    for _ in range(1000):
        # perform the broadcast
        low, high, affected = broadcaster.process("button", False)
        # update counters
        # +1 because we send a low to the broadcaster
        total_low += low+1
        total_high += high
        # queue of to be processed modules
        queue: list[tuple[str, str, bool]] = [("broadcaster", name, pulse) for name, pulse in affected]
        while queue:
            # get the oldest module to be processed
            src, module, pulse = queue.pop(0)
            # process the module
            low, high, affected = modules[module].process(src, pulse)
            # update the counters
            total_low += low
            total_high += high
            # extend the list of modules to be processed
            queue.extend([(module, name, pulse) for name, pulse in affected])
    print(total_low, total_high, total_low * total_high)
        
        
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
