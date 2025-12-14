import math
import os, sys
import time


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def dist(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))


class Cluster:
    def __init__(self):
        self.points = set()

    def add_point(self, point: Point):
        self.points.add(point)

    def min_dist(self, other: "Cluster") -> tuple[Point, Point, float]:
        min_distance = float("inf")
        closest_pair = (None, None)
        for p1 in self.points:
            for p2 in other.points:
                distance = p1.dist(p2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (p1, p2)
        if closest_pair[0] is None or closest_pair[1] is None:
            raise ValueError("No points in one of the clusters.")
        return closest_pair[0], closest_pair[1], min_distance

    def merge(self, other: "Cluster"):
        self.points.update(other.points)

    def is_in(self, point: Point) -> bool:
        return point in self.points

    def __len__(self):
        return len(self.points)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.points)


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    clusters: list[Cluster] = []
    points: list[Point] = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        point = Point(x, y, z)
        cluster = Cluster()
        cluster.add_point(point)
        clusters.append(cluster)
        points.append(point)
    last_connection = (None, None)
    while len(clusters) > 1:
        print(f"Clusters remaining: {len(clusters)}")
        min_distance = float("inf")
        to_merge = (None, None)
        mp1, mp2 = None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                p1, p2, distance = clusters[i].min_dist(clusters[j])
                if distance < min_distance:
                    min_distance = distance
                    mp1, mp2 = p1, p2
                    to_merge = (i, j)
        if to_merge[0] is not None and to_merge[1] is not None:
            last_connection = (mp1, mp2)
            clusters[to_merge[0]].merge(clusters[to_merge[1]])
            del clusters[to_merge[1]]

    print(f"Last connection: {last_connection[0]} <-> {last_connection[1]}")
    print(last_connection[0].x * last_connection[1].x)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
