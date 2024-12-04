import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    width = len(lines[0])
    height = len(lines)
    search_key = "MAS"
    search_len = len(search_key)
    counter = 0
    for i in range(width - search_len + 1):
        for j in range(height - search_len + 1):
            diag_right = "".join([lines[j+k][i+k] for k in range(search_len)])
            diag_left = "".join([lines[j+k][i+search_len-1-k] for k in range(search_len)])
            if (diag_right == search_key or diag_right == search_key[::-1]) and (diag_left == search_key or diag_left == search_key[::-1]):
                counter+=1
    print(counter)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
