import os, sys
import time

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def step(self, steps: int, width: int, height: int):
        for _ in range(steps):
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
    quadrants = [0, 0, 0, 0]
    for line in lines:
        p, v = line.split(" ")
        x, y = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robot = Robot(x, y, vx, vy)
        robot.step(seconds, width, height)
        robots.append(robot)
        if robot.x < width // 2:
            if robot.y < height // 2:
                quadrants[0] += 1
            elif robot.y > height // 2:
                quadrants[1] += 1
        elif robot.x > width // 2:
            if robot.y < height // 2:
                quadrants[2] += 1
            elif robot.y > height // 2:
                quadrants[3] += 1
    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
