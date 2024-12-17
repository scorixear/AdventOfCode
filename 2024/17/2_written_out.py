import os, sys
import time

class Program:
    def __init__(self, A: int, B: int, C: int, programm: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.programm = programm
        self.instruction_pointer = 0
        self.output: list[int] = []
def run(A: int):
    B = 0
    C = 0
    output: list[int] = []
    while True:
        # 2,4 => bst combo(4) => B = A % 8
        B = A % 8
        # 1,1 => bxl 1 => B = B ^ 1
        B = B ^ 1
        # 7,5 => cdv combo(5) => C = A // (2 ** 5)
        C = A // (2 ** B)
        # 1,5 => bxl 5 => B = B ^ 5
        B = B ^ 5
        # 4,2 => bxc => B = B ^ C
        B = B ^ C
        # 5,5 => out combo(5) => output += [B % 8]
        output.append(B % 8)
        # 0,3 => adv combo(3) => A = A // (2 ** 3)
        A = A // 8
        # 3,0 => jnz 0 => if A != 0: instruction_pointer = 0
        if A == 0:
            break
    return output
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    programm = list(map(int, lines[4].split(": ")[1].split(",")))  
    
    p_len = len(programm)
    digits = [0] * p_len
    current_index = p_len - 1
    previous_start = [0] * p_len
    while current_index >= 0:
        # calculate digit
        A = sum(digits[i] * (8 ** i) for i in range(p_len))
        # try all numbers
        found_digit = False
        for i in range(previous_start[current_index] + 1, 8):
            output = run(i * (8**current_index) + A)
            # test current digit
            if output[current_index] != programm[current_index]:
                continue
            digits[current_index] = i
            previous_start[current_index] = i
            found_digit = True
            break
        if not found_digit:
            digits[current_index] = 0
            digits[current_index + 1] = 0
            previous_start[current_index] = 0
            current_index += 1
        else:
            current_index -= 1
    A = sum(digits[i] * (8 ** i) for i in range(p_len))
    print(A)
    print(run(A))


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
