import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    result = 0
    for line in lines:
        first, last = None, None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        result += int(first + last)
    print(result)


if __name__ == "__main__":
  before = time.perf_counter()
  main()
  print(f"Time: {time.perf_counter() - before:.6f}s")