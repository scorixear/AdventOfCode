import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    max_size = 0
    points = []
    edges = []
    for i, line in enumerate(lines):
        points.append([int(x) for x in line.split(",")])
        if i > 0:
            edges.append((points[i - 1], points[i]))
    edges.append((points[-1], points[0]))  # Closing the loop

    max_size = 0
    for i in range(len(points) - 1):
        for j in range(i, len(points)):
            fromPoint = points[i]
            toPoint = points[j]
            minX, maxX = min(fromPoint[0], toPoint[0]), max(fromPoint[0], toPoint[0])
            minY, maxY = min(fromPoint[1], toPoint[1]), max(fromPoint[1], toPoint[1])
            dist = manhatten(fromPoint, toPoint)
            if dist * dist > max_size:
                if not intersections(minX, minY, maxX, maxY, edges):
                    area = (abs(fromPoint[0] - toPoint[0]) + 1) * (
                        abs(fromPoint[1] - toPoint[1]) + 1
                    )
                    if area > max_size:
                        max_size = area
    print(max_size)


def manhatten(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def intersections(minX, minY, maxX, maxY, edges):
    # check if inside the rectangle there are any edges
    # excluding the border, hence < and >
    for edge in edges:
        iMinX, iMaxX = min(edge[0][0], edge[1][0]), max(edge[0][0], edge[1][0])
        iMinY, iMaxY = min(edge[0][1], edge[1][1]), max(edge[0][1], edge[1][1])
        if minX < iMaxX and maxX > iMinX and minY < iMaxY and maxY > iMinY:
            return True
    return False


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
