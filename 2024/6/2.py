import enum
import os, sys
import time

class Direction(enum.Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3


class Guard:
    def __init__(self, pos: tuple[int, int], direction: Direction):
        self.pos = pos
        self.initial_pos = pos
        self.direction = direction
    
    def walkUntilExist(self, obstacles: set[tuple[int, int]]):
        x, y = self.pos
        curr_dir = self.direction
        visited: set[tuple[Direction, int, int]] = set()
        
        while True:
            if (curr_dir, x, y) in visited:
                return True
            visited.add((curr_dir, x, y))
            if curr_dir == Direction.NORTH:
                next_obstacle: tuple[int, int] | None = None
                for obs in obstacles:
                    if obs[0] == x and obs[1] < y:
                        if next_obstacle is None:
                            next_obstacle = obs
                        else:
                            if next_obstacle[1] < obs[1]:
                                next_obstacle = obs
                if next_obstacle is None:
                    return False
                y = next_obstacle[1] + 1
                curr_dir = Direction.EAST
            elif curr_dir == Direction.EAST:
                next_obstacle: tuple[int, int] | None = None
                for obs in obstacles:
                    if obs[1] == y and obs[0] > x:
                        if next_obstacle is None:
                            next_obstacle = obs
                        else:
                            if next_obstacle[0] > obs[0]:
                                next_obstacle = obs
                if next_obstacle is None:
                    return False
                x = next_obstacle[0] - 1
                curr_dir = Direction.SOUTH
            elif curr_dir == Direction.SOUTH:
                next_obstacle: tuple[int, int] | None = None
                for obs in obstacles:
                    if obs[0] == x and obs[1] > y:
                        if next_obstacle is None:
                            next_obstacle = obs
                        else:
                            if next_obstacle[1] > obs[1]:
                                next_obstacle = obs
                if next_obstacle is None:
                    return False
                y = next_obstacle[1] - 1
                curr_dir = Direction.WEST
            elif curr_dir == Direction.WEST:
                next_obstacle: tuple[int, int] | None = None
                for obs in obstacles:
                    if obs[1] == y and obs[0] < x:
                        if next_obstacle is None:
                            next_obstacle = obs
                        else:
                            if next_obstacle[0] < obs[0]:
                                next_obstacle = obs
                if next_obstacle is None:
                    return False
                x = next_obstacle[0] + 1
                curr_dir = Direction.NORTH

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    plane = [list(line) for line in lines]
    width = len(plane[0])
    height = len(plane)
    obstacles = set()
    current_pos: tuple[int, int] = (0, 0)
    facing_direction: Direction = Direction.NORTH
    for y in range(height):
        for x in range(width):
            if plane[y][x] == "#":
                obstacles.add((x, y))
            elif plane[y][x] == "^":
                current_pos = (x, y)
    guard = Guard(current_pos, facing_direction)
    counter = 0
    total_progress = width * height
    for y in range(height):
        for x in range(width):
            if plane[y][x] == ".":
                print(f"Checking {y*height + x + 1}/{total_progress} ({round((y*height + x + 1) / total_progress * 100)}%)", end="\r")
                new_obstacles = obstacles.copy()
                new_obstacles.add((x, y))
                is_loop = guard.walkUntilExist(new_obstacles)
                if is_loop:
                    #print(x, y)
                    counter += 1
    print()
    print(counter)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
