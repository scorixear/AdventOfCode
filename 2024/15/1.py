import os, sys
import time

class GridElement:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    def __eq__(self, other) -> bool:
        if isinstance(other, GridElement):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return False
class Box(GridElement):
    pass
class Wall(GridElement):
    pass
class Robot(GridElement):
    def move(self, direction: str, boxes: set[Box], walls: set[Wall], width: int, height: int):
        boxes_to_move = []
        dx, dy = 0, 0
        if direction == "^":
            dy = -1
        elif direction == "v":
            dy = 1
        elif direction == "<":
            dx = -1
        elif direction == ">":
            dx = 1
        else:
            return
        new_x, new_y = self.x + dx, self.y + dy
        can_move = False
        while new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
            if (new_x, new_y) in walls:
                can_move = False
                break
            if (new_x, new_y) in boxes:
                boxes_to_move.append(Box(new_x, new_y))
                new_x += dx
                new_y += dy
                continue
            can_move = True
            break
        if can_move:
            self.x += dx
            self.y += dy
            for box in boxes_to_move:
                boxes.remove(box)
            for box in boxes_to_move:
                boxes.add(Box(box.x + dx, box.y + dy))

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")

    robot: Robot = Robot(0, 0)
    boxes: set[Box] = set()
    walls: set[Wall] = set()
    read_grid = True
    y = 0
    width = 0
    height = 0
    for line in lines:
        if line == "":
            read_grid = False
            height = y
            print_grid(width, height, boxes, robot, walls)
            continue
        if read_grid:
            width = len(line)
            for x, char in enumerate(line):
                if char == "#":
                    walls.add(Wall(x, y))
                elif char == "@":
                    robot = Robot(x, y)
                elif char == "O":
                    box = Box(x, y)
                    boxes.add(box)
            y += 1
        else:
            for char in line:
                robot.move(char, boxes, walls, width, height)
                #print(char)
                #print_grid(width, height, boxes, robot, walls)
    print_grid(width, height, boxes, robot, walls)
    total = 0
    for box in boxes:
        total += 100*box.y + box.x
    print(total)

def print_grid(width: int, height: int, boxes: set[Box], robot: Robot, walls: set[Wall]):
    for y in range(height):
        for x in range(width):
            if (x, y) in boxes:
                print("O", end="")
            elif (x, y) == (robot.x, robot.y):
                print("@", end="")
            elif (x, y) in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
