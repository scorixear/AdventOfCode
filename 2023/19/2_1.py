import os, sys
import time
from RangeClasses import SortedRangeList

class Rule:
    def __init__(self, value: str, operation: bool, threshold: int, target: str):
        self.value = value
        self.operation = operation
        self.threshold = threshold
        self.target = target

class Workflow:
    def __init__(self, steps: list[Rule]):
        self.rules: list[Rule] = steps
    
    def split_range(self,
                    rule: Rule,
                    given_range: SortedRangeList,
                    range_index: int,
                    other_ranges: list[tuple[int, SortedRangeList]],
                    accepted: list[tuple[SortedRangeList, SortedRangeList, SortedRangeList, SortedRangeList]],
                    new_workflows: list[tuple[str, SortedRangeList, SortedRangeList, SortedRangeList, SortedRangeList]]):
        applied = SortedRangeList()
        not_applied = SortedRangeList()
        for s, e in given_range:
            if rule.operation:
                if s > rule.threshold:
                    applied.add_tuple((s, e))
                elif e <= rule.threshold:
                    not_applied.add_tuple((s, e))
                else:
                    applied.add_tuple((rule.threshold+1, e))
                    not_applied.add_tuple((s, rule.threshold+1))
            else:
                if e <= rule.threshold:
                    applied.add_tuple((s, e))
                elif s >= rule.threshold:
                    not_applied.add_tuple((s, e))
                else:
                    applied.add_tuple((s, rule.threshold))
                    not_applied.add_tuple((rule.threshold, e))
        if rule.target == "A" and len(applied) > 0:
            new_ranges = [None]*4
            new_ranges[range_index] = applied
            for i, r in other_ranges:
                new_ranges[i] = r.copy()
            accepted.append((new_ranges[0], new_ranges[1], new_ranges[2], new_ranges[3]))
            
        elif rule.target != "R" and len(applied) > 0:
            new_ranges = [None]*4
            new_ranges[range_index] = applied
            for i, r in other_ranges:
                new_ranges[i] = r.copy()
            new_workflows.append((rule.target, new_ranges[0], new_ranges[1], new_ranges[2], new_ranges[3]))
        
        if len(not_applied) > 0:
            return not_applied
        else:
            return None

    def perform_rules(self, x_range: SortedRangeList, m_range: SortedRangeList, a_range: SortedRangeList, s_range: SortedRangeList):
        accepted = []
        new_workflows = []
        for rule in self.rules:
            if rule.threshold is None:
                if rule.target == "A":
                    accepted.append((x_range.copy(), m_range.copy(), a_range.copy(), s_range.copy()))
                elif rule.target != "R":
                    new_workflows.append((rule.target, x_range.copy(), m_range.copy(), a_range.copy(), s_range.copy()))
                break
            if rule.value == "x":
                x_range = self.split_range(rule, x_range, 0, [(1, m_range), (2, a_range), (3, s_range)], accepted, new_workflows)
                if x_range is None:
                    break
            elif rule.value == "m":
                m_range = self.split_range(rule, m_range, 1, [(0, x_range), (2, a_range), (3, s_range)], accepted, new_workflows)
                if m_range is None:
                    break
            elif rule.value == "a":
                a_range = self.split_range(rule, a_range, 2, [(0, x_range), (1, m_range), (3, s_range)], accepted, new_workflows)
                if a_range is None:
                    break
            elif rule.value == "s":
                s_range = self.split_range(rule, s_range, 3, [(0, x_range), (1, m_range), (2, a_range)], accepted, new_workflows)
                if s_range is None:
                    break
        return accepted, new_workflows

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
        workflow_steps: list[Rule] = []
        # for each rule
        for step in steps:
            # split rule and target
            parts = step.split(":")
            # if no rule is given
            if len(parts) == 1:
                # add default rule
                workflow_steps.append(Rule(None, None, None, parts[0]))
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
                workflow_steps.append(Rule(value, operation, threshold, target))
        workflows[name] = Workflow(workflow_steps)

    workflow_queue: list[tuple[str, SortedRangeList, SortedRangeList, SortedRangeList, SortedRangeList]] = [
        ("in",
         SortedRangeList([(1, 4001)]),
         SortedRangeList([(1, 4001)]),
         SortedRangeList([(1, 4001)]),
         SortedRangeList([(1, 4001)]))]
    total = 0
    while workflow_queue:
        workflow_name, x_range, m_range, a_range, s_range = workflow_queue.pop()
        accepted, new_workflows = workflows[workflow_name].perform_rules(x_range, m_range, a_range, s_range)
        for x_range, m_range, a_range, s_range in accepted:
            x_values = 0
            for s, e in x_range:
                x_values += e-s
            m_values = 0
            for s, e in m_range:
                m_values += e-s
            a_values = 0
            for s, e in a_range:
                a_values += e-s
            s_values = 0
            for s, e in s_range:
                s_values += e-s
            total += x_values*m_values*a_values*s_values
        for workflow_name, x_range, m_range, a_range, s_range in new_workflows:
            workflow_queue.append((workflow_name, x_range, m_range, a_range, s_range))
    print(total)
        
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:0.6f} seconds")