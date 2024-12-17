import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    A = int(lines[0].split(": ")[1])
    B = int(lines[1].split(": ")[1])
    C = int(lines[2].split(": ")[1])
    
    programm = list(map(int, lines[4].split(": ")[1].split(",")))  
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(programm):
        opcode = programm[instruction_pointer]
        operand = programm[instruction_pointer + 1]
        # adv
        # Divide A / 2^combo(operand) = A
        if opcode == 0:
            A = A // 2**combo(operand, A, B, C)
        # bxl
        # bitwise XOR B with literal(operand) = B
        elif opcode == 1:
            B = B ^ operand
        # bst
        # B = combo(operand)%8
        elif opcode == 2:
            B = combo(operand, A, B, C) % 8
        # jnz
        # A = 0 -> nothing
        # instruction_pointer = literal(operand)
        elif opcode == 3:
            if A != 0:
                instruction_pointer = operand
                continue
        # bxc
        # bitwise XOR B and C = B
        elif opcode == 4:
            B = B ^ C
        # out
        # output combo(operand) % 8
        elif opcode == 5:
            output.append(combo(operand, A, B, C) % 8)
        # bdv
        # Divide A / 2^combo(operand) = B
        elif opcode == 6:
            B = A // 2**combo(operand, A, B, C)
        # cdv
        # Divide A / 2^combo(operand) = C
        elif opcode == 7:
            C = A // 2**combo(operand, A, B, C)
        else:
            raise ValueError("Invalid opcode")
        instruction_pointer += 2
    print(",".join(map(str, output)))
            
def combo(operand: int, a_register: int, b_register: int, c_register: int):
    if operand < 4:
        return operand
    if operand == 4:
        return a_register
    if operand == 5:
        return b_register
    if operand == 6:
        return c_register
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
