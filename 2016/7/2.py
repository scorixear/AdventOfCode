import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    count = 0
    is_hypernet = False
    for line in lines:
        area_broadcast_accessors = set()
        hypernets = set()
        curr_hypernet = ""
        for i in range(len(line)-2):
            if line[i] == "[":
                is_hypernet = True
                continue
            if line[i] == "]":
                is_hypernet = False
                hypernets.add(curr_hypernet)
                curr_hypernet = ""
                continue
            if is_hypernet:
                curr_hypernet += line[i]
            else:
                if line[i] == line[i+2] and line[i] != line[i+1]:
                    area_broadcast_accessors.add(line[i:i+3])
        for aba in area_broadcast_accessors:
            bab = aba[1] + aba[0] + aba[1]
            found_baba = False
            for hypernet in hypernets:
                if bab in hypernet:
                    found_baba = True
                    break
            if found_baba:
                count += 1
                break
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
