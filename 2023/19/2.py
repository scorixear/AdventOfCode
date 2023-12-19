from collections import deque
import os, sys
import time

class Workflow:
    def __init__(self, steps: list[tuple[str, bool, int, str]]):
        self.rules: list[tuple[str, bool, int, str]] = steps
    
    def apply_value(self, operation: str, threshold: int, low: int, high: int):
        # depending on the operation
        if operation == ">":
            # the range that applies to the rule
            # will be the range that is greater than the threshold
            low = max(low, threshold+1)
        elif operation == "<":
            # the range that applies to the rule
            # will be the range that is less than the threshold
            high = min(high, threshold)
        elif operation == ">=":
            # the range that applies to the rule
            # will be the range that is greater than or equal to the threshold
            low = max(low, threshold)
        else:
            # the range that applies to the rule
            # will be the range that is less than or equal to the threshold
            high = min(high, threshold+1)
        return low, high
    
    def check(self, x_l: int, x_h: int, m_l: int, m_h: int, a_l: int, a_h: int, s_l: int, s_h: int, workflow_queue: deque[tuple[str, int, int, int, int, int, int, int, int]]):
        # for each rule
        for value, operation, threshold, target in self.rules:
            # if no threshold is given
            if threshold == None:
                # add to the queue
                workflow_queue.appendleft((target, x_l, x_h, m_l, m_h, a_l, a_h, s_l, s_h))
                return
            op = ">" if operation else "<"
            # depending on each value of the rule
            if value == "x":
                # the region that satisfies the rule
                new_x_l, new_x_h = self.apply_value(op, threshold, x_l, x_h)
                # will be appended to the queue
                workflow_queue.append((target, new_x_l, new_x_h, m_l, m_h, a_l, a_h, s_l, s_h))
                # the region that does not satisfy the rule
                # will be checked in the next iteration
                x_l, x_h = self.apply_value("<=" if operation else ">=", threshold, x_l, x_h)
            elif value == "m":
                new_m_l, new_m_h = self.apply_value(op, threshold, m_l, m_h)
                workflow_queue.append((target, x_l, x_h, new_m_l, new_m_h, a_l, a_h, s_l, s_h))
                m_l, m_h = self.apply_value("<=" if operation else ">=", threshold, m_l, m_h)
            elif value == "a":
                new_a_l, new_a_h = self.apply_value(op, threshold, a_l, a_h)
                workflow_queue.append((target, x_l, x_h, m_l, m_h, new_a_l, new_a_h, s_l, s_h))
                a_l, a_h = self.apply_value("<=" if operation else ">=", threshold, a_l, a_h)
            else:
                new_s_l, new_s_h = self.apply_value(op, threshold, s_l, s_h)
                workflow_queue.append((target, x_l, x_h, m_l, m_h, a_l, a_h, new_s_l, new_s_h))
                s_l, s_h = self.apply_value("<=" if operation else ">=", threshold, s_l, s_h) 

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    workflows: dict[str, Workflow] = {}
    # workflow parsing
    for line in lines:
        # ignore items
        if line == "":
            break
        # split workflow name and rules
        name, steps = line.split("{", 1)
        # split rules by comma
        steps = steps[:-1].split(",")
        workflow_steps = []
        # for each rule
        for step in steps:
            # split rule and target
            parts = step.split(":")
            # if no rule is given
            if len(parts) == 1:
                # add default rule
                workflow_steps.append((None, None, None, parts[0]))
            # else add rule
            else:
                target = parts[1]
                # if rule is > comparison
                if ">" in parts[0]:
                    value, threshold = parts[0].split(">")
                    operation = True
                else:
                    value, threshold = parts[0].split("<")
                    operation = False
                threshold = int(threshold)
                workflow_steps.append((value, operation, threshold, target))
        workflows[name] = Workflow(workflow_steps)
    
    # contains workflows to be processed and their respective ranges
    workflow_queue: deque[tuple[str, int, int, int, int, int, int]] = deque([(
        "in", 1, 4001, 1, 4001, 1, 4001, 1, 4001)])
    total = 0
    # while we have more workflows to process
    while workflow_queue:
        # pop workflow and ranges
        workflow, x_l, x_h, m_l, m_h, a_l, a_h, s_l, s_h = workflow_queue.pop()
        # if the ranges are invalid, ignore
        if x_l > x_h or m_l > m_h or a_l > a_h or s_l > s_h:
            continue
        # if the workflow is accepted, add to total
        if workflow == "A":
            total += (x_h-x_l)*(m_h-m_l)*(a_h-a_l)*(s_h-s_l)
            continue
        # if the workflow is rejected, ignore
        if workflow == "R":
            continue
        workflow = workflows[workflow]
        # perform workflow
        workflow.check(x_l, x_h, m_l, m_h, a_l, a_h, s_l, s_h, workflow_queue)
    print(total)

        
                    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
