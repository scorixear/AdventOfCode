import dis
import enum
import os, sys
import time

class Direction(enum.Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3


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
    distinct_positions: set[tuple[int, int]] = set()
    for y in range(height):
        for x in range(width):
            if plane[y][x] == "#":
                obstacles.add((x, y))
            elif plane[y][x] == "^":
                current_pos = (x, y)
                distinct_positions.add(current_pos)
    while True:
        new_position = find_next_obstacle(current_pos, facing_direction, obstacles, width, height)
        add_positions(current_pos, facing_direction, distinct_positions, new_position, width, height)
        if new_position is None:
            break
        else:
            current_pos = new_position
            facing_direction = next_direction(facing_direction)
    print(len(distinct_positions))

def next_direction(direction: Direction):
    if direction == Direction.NORTH:
        return Direction.EAST
    elif direction == Direction.EAST:
        return Direction.SOUTH
    elif direction == Direction.SOUTH:
        return Direction.WEST
    return Direction.NORTH

def add_positions(current_pos: tuple[int, int], 
                  facing_direction: Direction, 
                  distinct_positions: set[tuple[int, int]], 
                  new_position: tuple[int, int] | None, 
                  width: int, 
                  height: int):
    x, y = current_pos
    if facing_direction == Direction.NORTH:
        for i in range(y, -1 if new_position is None else new_position[1] - 1, -1):
            distinct_positions.add((x, i))
    elif facing_direction == Direction.EAST:
        for i in range(x, width if new_position is None else new_position[0] + 1, 1):
            distinct_positions.add((i, y))
    elif facing_direction == Direction.SOUTH:
        for i in range(y, height if new_position is None else new_position[1] + 1, 1):
            distinct_positions.add((x, i))
    elif facing_direction == Direction.WEST:
        for i in range(x, -1 if new_position is None else new_position[0] - 1, -1):
            distinct_positions.add((i, y))

def find_next_obstacle(current_pos: tuple[int, int], 
                       facing_direction: Direction, 
                       obstacles: set[tuple[int, int]], 
                       width: int, 
                       height: int):
    x, y = current_pos
    if facing_direction == Direction.NORTH:
        for i in range(y - 1, -1, -1):
            if (x, i) in obstacles:
                return (x, i+1)
    elif facing_direction == Direction.EAST:
        for i in range(x + 1, width):
            if (i, y) in obstacles:
                return (i-1, y)
    elif facing_direction == Direction.SOUTH:
        for i in range(y + 1, height):
            if (x, i) in obstacles:
                return (x, i-1)
    elif facing_direction == Direction.WEST:
        for i in range(x - 1, -1, -1):
            if (i, y) in obstacles:
                return (i+1, y)
    return None

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
