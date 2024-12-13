import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")

    a_cost = 3
    b_cost = 1
    total = 0

    for i in range(0, len(lines), 4):
        a =  [int(l.split("+")[1]) for l in lines[i].split(":")[1].split(",")]
        ax, ay = a[0], a[1]
        b =  [int(l.split("+")[1]) for l in lines[i+1].split(":")[1].split(",")]
        bx, by = b[0], b[1]
        p =  [int(l.split("=")[1]) for l in lines[i+2].split(":")[1].split(",")]
        px, py = p[0] + 10000000000000, p[1] + 10000000000000

        det = bx * ay - ax * by
        if det == 0:
            continue
        bc = (ay * px - ax * py) / det
        ac = (bx * py - by * px) / det
        if round(bc) == bc and round(ac) == ac:
            total += a_cost * ac + b_cost * bc
        print(i)

    print(total)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
