import os, sys
import time
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    for line in lines:
        final_length = 0
        weights = [1]*len(line)
        i = 0
        while i < len(line):
            c = line[i]
            if c == "(":
                for j in range(i+1, len(line)):
                    if line[j] == ")":
                        break
                length, times = map(int, line[i+1:j].split("x"))
                for k in range(j+1, j+1+length):
                    weights[k] *= times
                i = j
            else:
                final_length += weights[i]
            i += 1
        print(final_length)
                

            
                
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
