import os, sys
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add(self, other):
        self.children.append(other)

    def search(self, target: "Node") -> int:
        dp = {}
        return self.dfs(target, dp)

    def dfs(self, target: "Node", dp: dict) -> int:
        if self.value in dp:
            return dp[self.value]
        if self == target:
            return 1
        total = 0
        for child in self.children:
            total += child.dfs(target, dp)
        dp[self.value] = total
        return total

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.value


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    nodes = {}
    start = Node(1)
    end = Node(1)
    for line in lines:
        parts = line.split(" ")
        value = parts[0][:-1]
        node = Node(value)
        if value in nodes:
            node = nodes[value]
        nodes[value] = node
        for other in parts[1:]:
            other_node = Node(other)
            if other in nodes:
                other_node = nodes[other]
            nodes[other] = other_node
            node.add(other_node)
            if other == "you":
                start = other_node
            if other == "out":
                end = other_node
        if value == "you":
            start = node
        if value == "out":
            end = node
    print(start.search(end))


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
