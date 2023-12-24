import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    points: list[tuple[list[int], list[int]]] = []
    for line in lines:
        pos, velo = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        velo = list(map(int, velo.split(", ")))
        points.append((pos, velo))
    counter = 0

    #match_range = [7, 27]
    match_range = [200000000000000, 400000000000000]
    pp = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            a1, a2 = points[i]
            x1 = a1[0]
            x2 = a1[0]+a2[0]
            y1 = a1[1]
            y2 = a1[1]+a2[1]
            b1, b2 = points[j]
            x3 = b1[0]
            x4 = b1[0]+b2[0]
            y3 = b1[1]
            y4 = b1[1]+b2[1]

            denominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
            #  den =     ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            if denominator != 0:
                px =   ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / denominator
                py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / denominator

                is_after_a = (px > x1) == (x2 > x1)
                is_after_b = (px > x3) == (x4 > x3)
                
                if is_after_a and is_after_b:
                    if match_range[0] <= px <= match_range[1] and match_range[0] <= py <= match_range[1]:
                        counter += 1
    print(counter)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
