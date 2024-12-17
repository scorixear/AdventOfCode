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
    def run(self):
        while self.instruction_pointer < len(self.programm):
            opcode = self.programm[self.instruction_pointer]
            operand = self.programm[self.instruction_pointer + 1]
            # adv
            if opcode == 0:
                self.A = self.A // 2**self.combo(operand)
            # bxl
            elif opcode == 1:
                self.B = self.B ^ operand
            # bst
            elif opcode == 2:
                self.B = self.combo(operand) % 8
            # jnz
            elif opcode == 3:
                if self.A != 0:
                    self.instruction_pointer = operand
                    continue
            # bxc
            elif opcode == 4:
                self.B = self.B ^ self.C
            # out
            elif opcode == 5:
                self.output.append(self.combo(operand) % 8)
            # bdv
            elif opcode == 6:
                self.B = self.A // 2**self.combo(operand)
            # cdv
            elif opcode == 7:
                self.C = self.A // 2**self.combo(operand)
            else:
                raise ValueError("Invalid opcode")
            self.instruction_pointer += 2
        return self.output
    def combo(self, operand: int):
        if operand < 4:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        else:
            raise ValueError("Invalid operator")

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    B = int(lines[1].split(": ")[1])
    C = int(lines[2].split(": ")[1])
    programm = list(map(int, lines[4].split(": ")[1].split(",")))
    
    # the desired length of the program
    p_len = len(programm)
    # the mod 8 digits of the number, per mod 8 digit, a new number is added to the output array
    digits = [0] * p_len
    # the current index of the digit we are trying out (starting from the right)
    current_index = p_len - 1
    # the previous numbers we tried out for each digit
    previous_start = [0] * p_len
    # loop until we found the number
    while current_index >= 0:
        # calculate current A without the current digit
        A = sum(digits[i] * (8 ** i) for i in range(p_len))
        found_digit = False
        # try all numbers for the current digit starting from the previous number we tried
        for i in range(previous_start[current_index] + 1, 8):
            # run the program with the current number
            runner = Program(i * (8**current_index) + A, B, C, programm)
            output = runner.run()
            # test current digit
            # only the current output digit and digits to the left will have changed
            # so no need to check the whole output array
            if output[current_index] != programm[current_index]:
                continue
            # we found a valid digit
            # set the digit and the previous start for the current digit
            digits[current_index] = i
            previous_start[current_index] = i
            found_digit = True
            break
        # if we didn't find a valid digit
        if not found_digit:
            # reset the current digit and the previously tried digit
            digits[current_index] = 0
            digits[current_index + 1] = 0
            # reset the previous start for the current digit
            previous_start[current_index] = 0
            # and backtrack to the previous digit to the right
            current_index += 1
        # if we found a valid digit
        # move to the next digit to the left
        else:
            current_index -= 1
    # calculate the final number
    A = sum(digits[i] * (8 ** i) for i in range(p_len))
    print(A)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
