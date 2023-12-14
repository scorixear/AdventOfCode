import os, sys
import time


dp = {}

def roll(grid: list[list[str]]):
    # move balls up
    # for each column
    for column in range(len(grid[0])):
        # for each row (maximum moves to the top is len(grid))
        for _ in range(len(grid)):
            # for each row
            for row, line in enumerate(grid):
                # if ball is below empty space
                if line[column] == "O" and row>0 and grid[row-1][column] == ".":
                    # roll up
                    grid[row-1][column] = "O"
                    line[column] = "."
def rotate(grid: list[list[str]]):
    # create new grid rotated 90 degrees clockwise
    new_grid = [["?" for _ in range(len(grid))] for _ in range(len(grid[0]))]
    # for each row
    for row, line in enumerate(grid):
        # for each column
        for column, char in enumerate(line):
            # position in new grid is column, len(grid)-1-row
            new_grid[column][len(grid)-1-row] = char
    return new_grid

def score(grid: list[list[str]]):
    result = 0
    # for each row
    for row, line in enumerate(grid):
        # for each column
        for char in line:
            # if ball
            if char == "O":
                # add the number of rows below
                result += len(grid) - row
    return result

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[char for char in line] for line in lines]
    # perform rolling of Up, Left, Down, Right
    for i in range(1_000_000_000):
        print(f"roll {i}")
        # if we have seen the roll before
        dp_key = tuple(tuple(row) for row in grid)
        if dp_key in dp:
            recurrent = dp[dp_key]
            # calculate the length of the cycle
            loop = i - recurrent
            # calculate remaining rolls after last occurrence of this roll
            a = (1_000_000_000 - i) % loop
            print(f"performing {a} additional rolls")
            for x in range(a):
                print(f"roll {x}")
                for _ in range(4):
                    roll(grid)
                    grid = rotate(grid)
            break
        # if we have not seen the roll before
        for _ in range(4):
            # perform rolling of Up, Left, Down, Right
            roll(grid)
            grid = rotate(grid)
        dp[dp_key] = i
    print(score(grid))
    
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
