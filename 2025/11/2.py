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
        return self.dfs(target, dp, False, False)

    def dfs(
        self, target: "Node", dp: dict, visited_fft: bool, visited_dac: bool
    ) -> int:
        if (self.value, visited_fft, visited_dac) in dp:
            return dp[(self.value, visited_fft, visited_dac)]
        if self == target:
            return 1 if visited_fft and visited_dac else 0
        total = 0
        for child in self.children:
            total += child.dfs(
                target,
                dp,
                self.value == "fft" or visited_fft,
                self.value == "dac" or visited_dac,
            )
        dp[(self.value, visited_fft, visited_dac)] = total
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
            if other == "svr":
                start = other_node
            if other == "out":
                end = other_node
        if value == "svr":
            start = node
        if value == "out":
            end = node
    print(start.search(end))


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
