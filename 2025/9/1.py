import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    max_size = 0
    points = []
    for line in lines:
        points.append([int(x) for x in line.split(",")])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            size = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if size > max_size:
                max_size = size
                print(f"New max size {max_size} from points {p1} and {p2}")
    print(max_size)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
