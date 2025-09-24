import os, sys
import time
from timeit import repeat

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    for line in lines:
        final_line = ""
        final_length = 0
        i = 0
        while i < len(line):
            c = line[i]
            if c == "(":
                marker = ""
                for j in range(i+1, len(line)):
                    if line[j] == ")":
                        break
                    marker += line[j]
                marker_parts = marker.split("x")
                repeat_counter = int(marker_parts[0])
                repeat_times = int(marker_parts[1])
                i = j + repeat_counter
                final_length += repeat_counter * repeat_times
                final_line += line[i-repeat_counter+1:i+1] * repeat_times
            else:
                final_length += 1
                final_line += c
            i += 1
        print(final_length)
        # print(final_line)

        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
