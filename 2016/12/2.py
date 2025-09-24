import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    register = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0
    }
    pointer = 0
    instructions = []
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "cpy":
            instructions.append(("cpy", parts[1], parts[2]))
        elif parts[0] == "jnz":
            instructions.append(("jnz", parts[1], int(parts[2])))
        else:
            instructions.append((parts[0], parts[1]))
    while pointer < len(instructions):
        inst = instructions[pointer]
        if inst[0] == "cpy":
            val = inst[1]
            if val in register:
                val = register[val]
            register[inst[2]] = int(val)
            pointer += 1
        elif inst[0] == "inc":
            register[inst[1]] += 1
            pointer += 1
        elif inst[0] == "dec":
            register[inst[1]] -= 1
            pointer += 1
        elif inst[0] == "jnz":
            val = inst[1]
            if val in register:
                val = register[val]
            else:
                val = int(val)
            offset = inst[2]
            if val != 0:
                pointer += offset
            else:
                pointer += 1
            if pointer < 0:
                raise Exception("Pointer out of bounds")
    print(register["a"])

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
