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
        a_x, a_y = a[0], a[1]
        b =  [int(l.split("+")[1]) for l in lines[i+1].split(":")[1].split(",")]
        b_x, b_y = b[0], b[1]
        p =  [int(l.split("=")[1]) for l in lines[i+2].split(":")[1].split(",")]
        p_x, p_y = p[0], p[1]

        #b_min = find_combi(a_x, a_y, b_x, b_y, p_x, p_y, a_cost, b_cost)
        #a_min = find_combi(b_x, b_y, a_x, a_y, p_x, p_y, b_cost, a_cost)
        #total += min(a_min, b_min)
        min_tokens = float("inf")
        for a_count in range(0, 101):
            for b_count in range(0, 101):
                current_x = a_count * a_x + b_count * b_x
                current_y = a_count * a_y + b_count * b_y
                if current_x == p_x and current_y == p_y:
                    min_tokens = min(min_tokens, a_count * a_cost + b_count * b_cost)
        if min_tokens == float("inf"):
            min_tokens = 0
        total += min_tokens

    print(total)

def find_combi(a_x: int, a_y: int, b_x: int, b_y: int, p_x: int, p_y: int, a_cost: int, b_cost: int):
    current_x = 0
    current_y = 0

    a_count = 0
    b_count = 0

    b_diff_x = p_x // b_x
    b_diff_y = p_y // b_y

    
    if b_diff_x < b_diff_y:
        b_count = b_diff_x
    else:
        b_count = b_diff_y
    if b_count > 100:
        b_count = 100
    b_count += 1
    current_x = b_count * b_x
    current_y = b_count * b_y

    while current_x != p_x and current_x != p_y:
        b_count -= 1
        current_x = b_count * b_x
        current_y = b_count * b_y
        if b_count < 0:
            return 0
        a_diff_x = (p_x - current_x) // a_x
        a_diff_y = (p_y - current_y) // a_y
        if a_diff_x < a_diff_y:
            a_count = a_diff_x
        else:
            a_count = a_diff_y
        while a_count == 0:
            b_count -= 1
            current_x -= b_x
            current_y -= b_y
            a_diff_x = (p_x - current_x) // a_x
            a_diff_y = (p_y - current_y) // a_y
            if a_diff_x < a_diff_y:
                a_count = a_diff_x
            else:
                a_count = a_diff_y
            if b_count == 0:
                break
        if a_count > 100:
            return 0
        current_x = b_count * b_x + a_count * a_x
        current_y = b_count * b_y + a_count * a_y
        

    print (a_count, b_count)
    return a_count * a_cost + b_count * b_cost

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
