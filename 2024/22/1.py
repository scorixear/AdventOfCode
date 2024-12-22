import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        number = int(line)
        for _ in range(2000):
            number = gen(number)
            #print(number)
        #print(number)
        total += number
    print(total)

def gen(number):
    # multiply by 64
    r1 = number << 6
    number ^= r1
    number %= 1<<24
    # divide by 32
    r2 = number >> 5
    number ^= r2
    number %= 1<<24
    # multiply by 2048
    r3 = number << 11
    number ^= r3
    number %= 1<<24
    return number

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
