import enum
import os, sys
import time

class Operator(enum.Enum):
    ADD = 0,
    MULT = 1,
    CONCAT = 2

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        target_str, number_str = line.split(": ")
        target = int(target_str)
        numbers = list(map(int, number_str.split(" ")))
        if find_calculation(target, numbers, []):
            total += target
    print(total)
        
def find_calculation(target: int, numbers: list[int], operators: list[Operator]):
    if len(operators) == len(numbers) - 1:
        return calculate(target, numbers, operators)
    next_operators = operators.copy()
    next_operators.append(Operator.ADD)
    if find_calculation(target, numbers, next_operators):
        return True
    next_operators[-1] = Operator.MULT
    if find_calculation(target, numbers, next_operators):
        return True
    next_operators[-1] = Operator.CONCAT
    if find_calculation(target, numbers, next_operators):
        return True
    return False

def calculate(target: int, numbers: list[int], operators: list[Operator]):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == Operator.ADD:
            result += numbers[i]
        elif operators[i - 1] == Operator.MULT:
            result *= numbers[i]
        else:
            result = int(str(result) + str(numbers[i]))
    return result == target
        
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
