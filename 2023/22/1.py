from functools import cmp_to_key
import os, sys
import time
import timeit

class Node:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        # coordinates are inclusive
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        # parents are bricks that are directly above this brick and touching
        self.parents: set["Node"] = set()
        # children are bricks that are directly below this brick and touching
        self.children: set["Node"] = set()
    def compare(self, other: "Node"):
        # compare bricks in ascending order, priority z, y, x
        if self.z1 == other.z1:
            if self.y1 == other.y1:
                return self.x1 - other.x1
            return self.y1 - other.y1
        return self.z1 - other.z1
    
    def fall(self, settled: list["Node"]):
        # if brick is at the ground, return
        if self.z1 == 1:
            return
        # find the highest brick that is directly below this brick and touching
        max_z = 0
        # touching_nodes is a list of bricks that are directly below this brick and touching
        touching_nodes = []
        # iterate through all settled bricks
        for node in settled:
            # if brick x1 coordinates is between settled brick x
            # or brick x2 coordinates is between settled brick x
            # or brick x1 is left and brick x2 is right of settled brick
            if node.x1 <= self.x1 <= node.x2 or node.x1 <= self.x2 <= node.x2 or (node.x1 > self.x1 and node.x2 < self.x2):
                # if brick y1 coordinates is between settled brick y
                # or brick y2 coordinates is between settled brick y
                # or brick y1 is left and brick y2 is right of settled brick
                if node.y1 <= self.y1 <= node.y2 or node.y1 <= self.y2 <= node.y2 or (node.y1 > self.y1 and node.y2 < self.y2):
                    # if settled brick is same height as current max_z
                    if max_z == node.z2+1:
                        # append to touching_nodes
                        touching_nodes.append(node)
                    # if settled brick is higher than current max_z
                    # all other touching nodes will not touch this brick
                    elif max_z < node.z2+1:
                        max_z = node.z2+1
                        touching_nodes = [node]
        # if no settled bricks found
        # brick falls to ground
        if max_z == 0:
            diff = self.z2 - self.z1
            self.z1 = 1
            self.z2 = 1 + diff
        # if settled bricks found
        else:
            # for each touching node, add brick to parent and add touching node to child
            for node in touching_nodes:
                node.parents.add(self)
                self.children.add(node)
            # set brick to new height
            diff = self.z2 - self.z1
            self.z1 = max_z
            self.z2 = max_z + diff
    def can_remove(self):
        # for each parent
        for parent in self.parents:
            # if parent is only touching this brick
            # this cannot be removed
            if len(parent.children) == 1:
                return False
        return True

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
        
    bricks: list[Node] = []
    # parse blocks
    for line in lines:
        a, b = line.split("~")
        a_coords = list(map(int, a.split(",")))
        b_coords = list(map(int, b.split(",")))
        # coordinates are inclusive
        # best coordinate is diagonal corners
        min_x, min_y, min_z = min(a_coords[0], b_coords[0]), min(a_coords[1], b_coords[1]), min(a_coords[2], b_coords[2])
        max_x, max_y, max_z = max(a_coords[0], b_coords[0]), max(a_coords[1], b_coords[1]), max(a_coords[2], b_coords[2])
        bricks.append(Node(min_x, min_y, min_z, max_x, max_y, max_z))
    # sort bricks in ascending order, priority z, y, x
    bricks.sort(key=cmp_to_key(lambda a, b: a.compare(b)))

    settled = []
    for brick in bricks:
        # let brick fall until it hits settled or ground
        brick.fall(settled)
        settled.append(brick)
    bricks = settled

    count = 0
    for brick in bricks:
        # check if brick can be removed
        if brick.can_remove():
            count += 1
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")

    print(f"Avg: {timeit.timeit(main, number=1000)/1000:.6f}s")