from enum import Enum
import os, sys
from queue import PriorityQueue
import time

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

class WalkInfo():
    def __init__(self, cost: int, x: int, y: int, direction: Direction, step_counter: int):
        self.cost = cost
        self.x = x
        self.y = y
        self.direction = direction
        self.step_counter = step_counter
    # most important is cost when dequeueing
    # as dijkstra needs minimum cost for next step
    def __lt__(self, other):
        if self.cost == other.cost:
            if self.x == other.x:
                if self.y == other.y:
                    if self.direction == other.direction:
                        return self.step_counter < other.step_counter
                    return self.direction.value < other.direction.value
                return self.y < other.y
            return self.x < other.x
        return self.cost < other.cost
    # more equality functions as I don't have any idea what PriorityQueue needs
    def __eq__(self, other):
        return self.cost == other.cost and self.x == other.x and self.y == other.y and self.direction == other.direction and self.step_counter == other.step_counter
    def __hash__(self):
        return hash((self.cost, self.x, self.y, self.direction, self.step_counter))
    def __gt__(self, other) -> bool:
        if self.cost == other.cost:
            if self.x == other.x:
                if self.y == other.y:
                    if self.direction == other.direction:
                        return self.step_counter > other.step_counter
                    return self.direction.value > other.direction.value
                return self.y > other.y
            return self.x > other.x
        return self.cost > other.cost
    def __le__(self, other) -> bool:
        return self < other or self == other
    def __ge__(self, other) -> bool:
        return self > other or self == other
    def __ne__(self, other) -> bool:
        return not self == other
    # for hashing the visited set
    # no idea why custom class didn't work
    def get_visited_info(self):
        return (self.x, self.y, self.direction, self.step_counter)

def dijkstra(graph: list[list[int]], max_steps: int):
    queue: PriorityQueue[WalkInfo] = PriorityQueue()
    # initialize priority queue with the first two directions
    # step counter is set to 1, as we will take 1 step in that direction
    queue.put(WalkInfo(0, 0, 0, Direction.RIGHT, 1))
    queue.put(WalkInfo(0, 0, 0, Direction.DOWN, 1))
    # tuple for hashing, cost not important here
    visited: set[tuple[int, int, Direction, int]] = set()
    
    while queue:
        # get most important cell (lowest cost)
        curr: WalkInfo = queue.get()
        # if already seen in this configuration, skip
        if curr.get_visited_info() in visited:
            continue
        visited.add(curr.get_visited_info())
        
        # calculate next position
        new_x = curr.x + curr.direction.value[1]
        new_y = curr.y + curr.direction.value[0]
        # if position is outside grid, skip
        if new_x < 0 or new_x >= len(graph[0]) or new_y < 0 or new_y >= len(graph):
            continue
        # new cost
        new_cost = curr.cost + graph[new_y][new_x]
        # if we reached the end, and didn't use too many steps, return the cost
        if curr.step_counter <= max_steps and new_x == len(graph[0]) - 1 and new_y == len(graph) - 1:
            return new_cost
        # for each direction
        for new_direction in Direction:
            # if the new direction is the opposite of the current direction, skip
            if new_direction.value[0] + curr.direction.value[0] == 0 and new_direction.value[1] + curr.direction.value[1] == 0:
                continue
            # if new direction is the same, increase step counter, otherwise set to 1
            if new_direction == curr.direction:
                new_step_counter = curr.step_counter + 1
            else:
                new_step_counter = 1
            # if new step counter is too high, skip
            if new_step_counter > max_steps:
                continue
            queue.put(WalkInfo(new_cost, new_x, new_y, new_direction, new_step_counter))
    return -1
    

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[int(num) for num in line] for line in lines]
    
    print(dijkstra(grid, 3))

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:0.6f} seconds")