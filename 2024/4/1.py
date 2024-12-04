from re import search
import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    search_key = "XMAS"
    width = len(lines[0])
    height = len(lines)
    search_len = len(search_key)
    # horizontal search
    counter = 0
    for line in lines:
        for i in range(width - search_len + 1):
            word = line[i:i+search_len]
            if word == search_key or word == search_key[::-1]:
                counter+=1 
    # vertical search
    for i in range(width):
        for j in range(height - search_len + 1):
            word = "".join([lines[j+k][i] for k in range(search_len)])
            if word == search_key or word == search_key[::-1]:
                counter+=1
    # diagonal right search
    for i in range(width - search_len + 1):
        for j in range(height - search_len + 1):
            word = "".join([lines[j+k][i+k] for k in range(search_len)])
            if word == search_key or word == search_key[::-1]:
                counter+=1
    # diagonal left search
    for i in range(search_len - 1, width):
        for j in range(height - search_len + 1):
            word = "".join([lines[j+k][i-k] for k in range(search_len)])
            if word == search_key or word == search_key[::-1]:
                counter+=1
    print(counter)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
