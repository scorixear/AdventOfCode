import math
import os, sys
import time


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.cluster = None

    def dist(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def add_to_cluster(self, cluster: "Cluster"):
        self.cluster = cluster

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
        point.add_to_cluster(self)

    def min_dist(self, other: "Cluster") -> float:
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
        return min_distance

    def merge(self, other: "Cluster"):
        self.points.update(other.points)
        for point in other.points:
            point.add_to_cluster(self)

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
    visited = set()
    for x in range(1000):
        print(f"Iteration {x+1}")
        min_distance = float("inf")
        to_merge = (None, None)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if (i, j) in visited:
                    continue
                distance = points[i].dist(points[j])
                if distance < min_distance and (i, j) not in visited:
                    min_distance = distance
                    to_merge = (i, j)
        if to_merge[0] is not None and to_merge[1] is not None:
            visited.add(to_merge)
            # print(
            #     f"Merging points {points[to_merge[0]]} and {points[to_merge[1]]} with distance {min_distance:.4f}"
            # )
            if points[to_merge[0]].cluster != points[to_merge[1]].cluster:
                del clusters[clusters.index(points[to_merge[1]].cluster)]
                points[to_merge[0]].cluster.merge(points[to_merge[1]].cluster)

    sorted_clusters = sorted(clusters, key=len, reverse=True)
    print(len(sorted_clusters[0]) * len(sorted_clusters[1]) * len(sorted_clusters[2]))


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
