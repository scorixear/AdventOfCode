import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
        message = ""
        most_commons = [{} for _ in range(len(lines[0]))]
        for line in lines:
            for i, char in enumerate(line):
                if char not in most_commons[i]:
                    most_commons[i][char] = 0
                most_commons[i][char] += 1
        for most_common in most_commons:
            letters = sorted(most_common.items(), key=lambda x: x[1])
            message += letters[0][0]
        print(message)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
