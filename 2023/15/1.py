import os, sys
import time

def hash(sequence: str) -> int:
    curr = 0
    # for each char
    for c in sequence:
        # get ascii value
        curr += ord(c)
        # multiply by 17
        curr *= 17
        # and mod by 256
        curr %= 256
    return curr

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    sequences = text.split(",")
    total = 0
    # hash each sequence and add up results
    for sequence in sequences:
        total += hash(sequence)
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
