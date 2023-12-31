import os, sys
import time
import timeit

class Light:
    def __init__(self, x, y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx, dy
    def move(self, grid: list[str]) -> tuple[list["Light"], bool]:
        if (self.x + self.dx) >= len(grid[0]) or (self.x + self.dx) < 0 or (self.y + self.dy) >= len(grid) or (self.y + self.dy) < 0:
            return []
        if grid[self.y + self.dy][self.x + self.dx] == ".":
            self.x += self.dx
            self.y += self.dy
            return [self]
        if grid[self.y + self.dy][self.x + self.dx] == "/":
            self.x += self.dx
            self.y += self.dy
            if self.dx == 1:
                self.dx = 0
                self.dy = -1
            elif self.dx == -1:
                self.dx = 0
                self.dy = 1
            elif self.dy == 1:
                self.dx = -1
                self.dy = 0
            elif self.dy == -1:
                self.dx = 1
                self.dy = 0
            return [self]
        if grid[self.y + self.dy][self.x + self.dx] == "\\":
            self.x += self.dx
            self.y += self.dy
            if self.dx == 1:
                self.dx = 0
                self.dy = 1
            elif self.dx == -1:
                self.dx = 0
                self.dy = -1
            elif self.dy == 1:
                self.dx = 1
                self.dy = 0
            elif self.dy == -1:
                self.dx = -1
                self.dy = 0
            return [self]
        if grid[self.y + self.dy][self.x + self.dx] == "-":
            self.x += self.dx
            self.y += self.dy
            if self.dx in (1, -1):
                return [self]
            self.dx = 1
            self.dy = 0
            return [self, Light(self.x, self.y, -1, 0)]
        if grid[self.y + self.dy][self.x + self.dx] == "|":
            self.x += self.dx
            self.y += self.dy
            if self.dy in (1, -1):
                return [self]
            self.dx = 0
            self.dy = 1
            return [self, Light(self.x, self.y, 0, -1)]
        return []
    
    def __hash__(self):
        return hash((self.x, self.y, self.dx, self.dy))
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.dx}, {self.dy})"

    def __repr__(self) -> str:
        return str(self)
    
    def get_d(self) -> tuple[int, int]:
        return (self.dx, self.dy)
    
def traverse_light(grid: list[str], start: Light) -> tuple[int, set[tuple[int, int]]]:
    encountered = [[set() for _ in  range(len(grid[0]))] for _ in range(len(grid))]
    lights = [start]
    enlightened = set()
    while lights:
        curr = lights.pop()
        new_lights = curr.move(grid)
        for light in new_lights:
            enlightened.add((light.x, light.y))
            if light.get_d() in encountered[light.y][light.x]:
                continue
            encountered[light.y][light.x].add(light.get_d())
            lights.append(light)
    return len(enlightened)
    
 
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    max_enlightened = 0
    for y in range(len(lines)):
        max_enlightened = max(max_enlightened, traverse_light(lines, Light(len(lines[0]), y, -1, 0)), traverse_light(lines, Light(-1, y, 1, 0)))
    for x in range(len(lines)):
        max_enlightened = max(max_enlightened, traverse_light(lines, Light(x, len(lines), 0, -1)), traverse_light(lines, Light(x, -1, 0, 1)))
    print(max_enlightened)
   
        
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
    
    print(f"Avg: {timeit.timeit(main, number=100)/100:.6f}")
