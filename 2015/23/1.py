import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    program_counter = 0
    registers = {"a": 0, "b": 0}
    
    while program_counter < len(lines):
        instruction, other = lines[program_counter].split(" ", 1)
        if instruction == "hlf":
            registers[other] //= 2
        elif instruction == "tpl":
            registers[other] *= 3
            # possible overflow?
        elif instruction == "inc":
            registers[other] += 1
            # overflow
        elif instruction == "jmp":
            program_counter += int(other)
            continue
        elif instruction == "jie":
            register, offset = other.split(", ", 1)
            if registers[register] % 2 == 0:
                program_counter += int(offset)
                continue
        elif instruction == "jio":
            register, offset = other.split(", ", 1)
            if registers[register] == 1:
                program_counter += int(offset)
                continue
        program_counter +=1
    print(registers["b"])
