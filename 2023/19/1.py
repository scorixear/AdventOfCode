import os, sys
import time

class Item:
    def __init__(self, x: int, m: int, a: int, s: int):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

class Workflow:
    def __init__(self, steps: list[tuple[str, bool, int, str]]):
        self.steps: list[tuple[str, bool, int, str]] = steps
    
    def check(self, item: Item):
        is_rejected = False
        next_workflow = None
        for (value, operation, threshold, target) in self.steps:
            if threshold == None:
                if target == "R":
                    is_rejected = True
                    break
                if target == "A":
                    break
                next_workflow = target
                break
            item_value = getattr(item, value)
            if operation:
                if item_value > threshold:
                    if target == "R":
                        is_rejected = True
                        break
                    if target == "A":
                        break
                    next_workflow = target
                    break
            else:
                if item_value < threshold:
                    if target == "R":
                        is_rejected = True
                        break
                    if target == "A":
                        break
                    next_workflow = target
                    break
        return (next_workflow, is_rejected)



def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    workflows: dict[str, Workflow] = {}
    items: list[tuple(Item, str)] = []
    init_workflow = True
    for line in lines:
        if line == "":
            init_workflow = False
            continue
        if init_workflow:
            name, steps = line.split("{", 1)
            steps = steps[:-1].split(",")
            workflow_steps = []
            for step in steps:
                parts = step.split(":")
                if len(parts) == 1:
                    workflow_steps.append((None, None, None, parts[0]))
                else:
                    target = parts[1]
                    if ">" in parts[0]:
                        value, threshold = parts[0].split(">")
                        operation = True
                    else:
                        value, threshold = parts[0].split("<")
                        operation = False
                    threshold = int(threshold)
                    workflow_steps.append((value, operation, threshold, target))
            workflows[name] = Workflow(workflow_steps)
        else:
            values = line[1:-1].split(",")
            int_values = []
            for value in values:
                int_values.append(int(value.split("=")[1]))
            items.append((Item(int_values[0], int_values[1], int_values[2], int_values[3]), "in"))
            
    accepted_items = []
    while items:
        item, workflow_name = items.pop()
        new_workflow, is_rejected = workflows[workflow_name].check(item)
        if new_workflow:
            items.append((item, new_workflow))
        elif not is_rejected:
            accepted_items.append(item)
    total = 0
    for item in accepted_items:
        total += item.x+item.m+item.a+item.s
    print(total)
        
            
                    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
