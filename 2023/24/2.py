import os, sys
import time
from z3 import Int, Solver
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    points: list[list[int]] = []
    for line in lines:
        pos, velo = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        velo = list(map(int, velo.split(", ")))
        points.append(pos + velo)

    x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
    T = [Int(f'T{i}') for i in range(len(points))]
    SOLVE = Solver()
    for i in range(len(points)):
      SOLVE.add(x + T[i]*vx - points[i][0] - T[i]*points[i][3] == 0)
      SOLVE.add(y + T[i]*vy - points[i][1] - T[i]*points[i][4] == 0)
      SOLVE.add(z + T[i]*vz - points[i][2] - T[i]*points[i][5] == 0)
    res = SOLVE.check()
    M = SOLVE.model()
    print(M.eval(x+y+z))

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
