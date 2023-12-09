import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    count = 0
    is_hypernet = False
    for line in lines:
        count_ip = False
        for i in range(len(line)-3):
            if "[" in line[i:i+4]:
                is_hypernet = True
                continue
            if "]" in line[i:i+4]:
                is_hypernet = False
                continue
            if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
                if is_hypernet:
                    count_ip = False
                    break
                count_ip = True
        if count_ip:
            # print(line)
            count += 1
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
