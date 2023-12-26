import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    result = 0
    digits = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in lines:
        first, last = None, None
        for i,c in enumerate(line):
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)
            else:
                if i < len(line) - 2 and line[i:i+3] in digits:
                    if first is None:
                        first = digits[line[i:i+3]]
                    last = digits[line[i:i+3]]
                    continue
                if i < len(line) - 3 and line[i:i+4] in digits:
                    if first is None:
                        first = digits[line[i:i+4]]
                    last = digits[line[i:i+4]]
                    continue
                if i < len(line) - 4 and line[i:i+5] in digits:
                    if first is None:
                        first = digits[line[i:i+5]]
                    last = digits[line[i:i+5]]
                    continue
        result += first*10 + last
    print(result)



if __name__ == "__main__":
  before = time.perf_counter()
  main()
  print(f"Time: {time.perf_counter() - before:.6f}s")
