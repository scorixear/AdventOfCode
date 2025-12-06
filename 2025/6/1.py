import os, sys
import time


class Problem:
    def __init__(self, expression: str, start: int):
        self.expression = expression
        self.start = start
        self.end = start
        self.numbers = []

    def set_end(self, end: int):
        self.end = end

    def add_numbers(self, lines: list[str]):
        for line in lines:
            number = int(line[self.start : self.end].strip())
            self.numbers.append(number)

    def solve(self):
        if self.expression == "+":
            return sum(self.numbers)
        elif self.expression == "*":
            result = 1
            for number in self.numbers:
                result *= number
            return result
        else:
            raise ValueError(f"Unknown expression: {self.expression}")

    def __repr__(self):
        return f"{self.expression}({self.start}-{self.end}): {self.numbers}"


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    operands = lines[-1]
    problems: list[Problem] = []
    for i, c in enumerate(operands):
        if c != " ":
            problem = Problem(c, i)
            if len(problems) > 0:
                problems[-1].set_end(i)
            problems.append(problem)
    problems[-1].set_end(max_len)
    total = 0
    for problem in problems:
        problem.add_numbers(lines[:-1])
        total += problem.solve()
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
