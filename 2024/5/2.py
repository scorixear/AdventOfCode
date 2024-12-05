from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt
import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    rules: list[tuple[int, int]] = []
    rule_list: dict[int, list[int]] = {}
    prints: list[list[int]] = []
    total = 0
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            ai, bi = int(a), int(b)
            rules.append((ai, bi))
            if ai not in rule_list:
                rule_list[ai] = []
            rule_list[ai].append(bi)
        elif line.strip() != "":
            prints.append(list(map(int, line.split(","))))
    for numbers in prints:
        if not is_valid(numbers, rule_list):
            keyed_rules = topological_order(rules, numbers)
            sorted_numbers = sort(numbers, keyed_rules)
            middle = sorted_numbers[len(sorted_numbers) // 2]
            total += middle

    print(total)

def topological_order(rules: list[tuple[int, int]], numbers: list[int]) -> dict[int, int]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in rules:
        if a not in numbers or b not in numbers:
            continue
        graph[b].append(a)
        in_degree[a] += 1
        if b not in in_degree:
            in_degree[b] = 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return {value: index for index, value in enumerate(order)}

def sort(numbers: list[int], keyed_rules: dict[int, int]) -> list[int]:
    return sorted(numbers, key=lambda x: keyed_rules.get(x, float("inf")))
def is_valid(numbers: list[int], rules: dict[int, list[int]]) -> bool:
    new_dict: dict[int, int] = {}
    for i, number in enumerate(numbers):
        new_dict[number] = i
    is_valid = True
    for i, number in enumerate(numbers):
        if number in rules:
            afters = rules[number]
            all_matched = True
            for after in afters:
                if after in new_dict:
                    if new_dict[after] < i:
                        all_matched = False
                        break
            if not all_matched:
                is_valid = False
                break
    return is_valid
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
