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
class BoxSet(set[Box]):
    def overlaps(self, box: tuple[int, int]) -> Box | None:
        for b in self:
            if b.x == box[0] and b.y == box[1]:
                return b
            if b.x == box[0]- 1 and b.y == box[1]:
                return b
        return None
class Wall(GridElement):
    pass
class Robot(GridElement):
    def move(self, direction: str, boxes: BoxSet, walls: set[Wall], width: int, height: int):
        boxes_to_move = set()
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
        new_pos = set([(self.x + dx, self.y + dy)])
        can_move = True
        while True:
            should_break = False
            next_pos = set()
            for new_x, new_y in new_pos:
                if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                    should_break = True
                    can_move = False
                    break
                if (new_x, new_y) in walls:
                    should_break = True
                    can_move = False
                    break
                box = boxes.overlaps((new_x, new_y))
                if box is not None:
                    boxes_to_move.add(box)
                    next_pos.add((box.x + dx, box.y + dy))
                    next_pos.add((box.x + 1 + dx, box.y + dy))
                    continue
            if should_break:
                break
            if len(next_pos) == 0:
                can_move = True
                break
            if next_pos == new_pos:
                break
            new_pos = next_pos
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
    boxes: BoxSet = BoxSet()
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
            width = len(line)*2
            for x, char in enumerate(line):
                if char == "#":
                    walls.add(Wall(x*2, y))
                    walls.add(Wall(x*2+1, y))
                elif char == "@":
                    robot = Robot(x*2, y)
                elif char == "O":
                    box = Box(x*2, y)
                    boxes.add(box)
            y += 1
        else:
            for char in line:
                robot.move(char, boxes, walls, width, height)
                # print(char)
                # print_grid(width, height, boxes, robot, walls)
    print_grid(width, height, boxes, robot, walls)
    total = 0
    for box in boxes:
        total += 100*box.y + box.x
    print(total)

def print_grid(width: int, height: int, boxes: BoxSet, robot: Robot, walls: set[Wall]):
    for y in range(height):
        x = 0
        while x < width:
            box = boxes.overlaps((x, y))
            if box is not None:
                print("[", end="")
                print("]", end="")
                x += 1
            elif (x, y) == (robot.x, robot.y):
                print("@", end="")
            elif (x, y) in walls:
                print("#", end="")
            else:
                print(".", end="")
            x += 1
        print()
    print()
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
