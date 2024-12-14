import os, sys
import time

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def step(self, width: int, height: int):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x += width
        elif self.x >= width:
            self.x -= width
        if self.y < 0:
            self.y += height
        elif self.y >= height:
            self.y -= height
           
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")

    seconds = 100
    width = 101 #11
    height = 103 #7
    robots = []
    for line in lines:
        p, v = line.split(" ")
        x, y = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robot = Robot(x, y, vx, vy)
        robots.append(robot)
    seconds_counter = 1
    max_neighbours = 0
    while True:
        robot_positions: set[tuple[int, int]] = set()
        for robot in robots:
            robot.step(width, height)
            robot_positions.add((robot.x, robot.y))
        
        neighbour_count = 0
        for x, y in robot_positions:
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in robot_positions:
                    neighbour_count += 1
                    break
        if neighbour_count > max_neighbours:
            input("Press Enter to continue...")
            max_neighbours = neighbour_count
            grid = [[" " for _ in range(width)] for _ in range(height)]
            for robot in robots:
                grid[robot.y][robot.x] = "#"
            for row in grid:
                print("".join(row))
            print(seconds_counter)
        seconds_counter += 1



if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
