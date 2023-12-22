import os, sys
import time
def get_start(grid: list[list[str]]):
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c == "S":
                grid[y][x] = "."
                return (x,y)

def bfs(grid: list[list[str]], start: tuple[int, int], max_steps: int):
    # quadratic formula, three factors a, b, c for y = a + bx + cx^2
    factors = [0, 0, 0]
    # index of factor to set
    factor_index = 0
    # set of positions to check
    positions = {start}
    # directions to travel to
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    # size of grid (is square)
    n = len(grid)
    
    target = n//2
    
    # take first 1000 steps to get three distinct points on the quadratic curve
    for step in range(1, 1000):
        new_positions = set()
        # for each position to be observed
        for x,y in positions:
            # take step in each direction
            for dx,dy in directions:
                new_x = x + dx
                new_y = y + dy
                # if the new position is a garden
                if grid[new_y%n][new_x%n] != "#":
                    # add it to the set of positions to be observed
                    new_positions.add((new_x, new_y))
        positions = new_positions
        # if we reached a new repetition, which is n steps away, starting from n//2 (full grid added)
        if step == target + n*factor_index:
            # get the number of positions reached
            factors[factor_index] = len(positions)
            # increment the factor index
            factor_index += 1
            # if we have all three factors, we can calculate the quadratic formula
            if factor_index == 3:
                # the factors are actually the rate of change of the number of reached positions
                # therefore, a is linearly the increase from 0 to n//2
                # b is the rate of change from n//2 to n+n//2
                # and c must be the rate of change of the rate of change, meaning (f2 - f1) - (f1 - f0)
                a, b, c = factors[0], factors[1]-factors[0], factors[2]-2*factors[1]+factors[0]
                # x represents the number of grids added
                # therefore x = max_steps//n
                # this isn't x^2, but rather x * (x-1) / 2, since x^2 would be the number of positions reached
                # when moving diagonally, which is not the case
                return a + b*(max_steps//n) + c * ((max_steps//n) * ((max_steps//n) - 1) // 2)
    # if we didn't reach the quadratic formula, we can't calculate the number of reached positions
    return -1

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[c for c in line] for line in lines]
    
    starting_pos = get_start(grid)
    steps = 26501365
    # n = len(lines)
    # print(starting_pos)
    # print(steps // n, steps % n)
    # steps = 202300 * 131 + 65
    print(bfs(grid, starting_pos, steps))
    #print(bfs(lines, starting_pos, 5000))
    
    
        
                
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
