from enum import Enum
import os, sys
import time

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Roller:
    def __init__(self, stoppers, rows, columns) -> None:
        self.stoppers = stoppers
        self.rows = rows
        self.columns = columns
        self.dp = {}

    def roll(self, balls: list[tuple[int, int]], edge: int, direction: Direction):
        # new position of balls stored here
        new_balls = []
        # define helper functions for each direction
        if direction == Direction.UP:
            # check if on the same row and after given o_y
            def is_after(x, y, o_x, o_y):
                return x == o_x and y >= o_y
            # move column one down
            def update_pos(x, y):
                return (x, y + 1)
            # set new max column
            def set_max(x, y, _, o_y):
                return (x, max(o_y, y))
            # set column to minimal value
            def set_edge(x, _):
                return (x, edge)
        elif direction == Direction.DOWN:
            # check if on the same row and before given o_y
            def is_after(x, y, o_x, o_y):
                return x == o_x and y <= o_y
            # move column one up
            def update_pos(x, y):
                return (x, y - 1)
            # set new min column
            def set_max(x, y, _, o_y):
                return (x, min(o_y, y))
            # set column to maximal value
            def set_edge(x, _):
                return (x, edge)
        elif direction == Direction.LEFT:
            # check if on the same column and after given o_x
            def is_after(x, y, o_x, o_y):
                return y == o_y and x >= o_x
            # move row one right
            def update_pos(x, y):
                return (x + 1, y)
            # set new max row
            def set_max(x, y, o_x, _):
                return (max(o_x, x), y)
            # set row to minimal value
            def set_edge(_, y):
                return (edge, y)
        else:
            # check if on the same column and before given o_x
            def is_after(x, y, o_x, o_y):
                return y == o_y and x <= o_x
            # move row one left
            def update_pos(x, y):
                return (x - 1, y)
            # set new min row
            def set_max(x, y, o_x, _):
                return (min(o_x, x), y)
            # set row to maximal value
            def set_edge(_, y):
                return (edge, y)
        # for each ball to roll
        for ball_x, ball_y in balls:
            # set possible position to be at the edge (greedy)
            new_x, new_y = set_edge(ball_x, ball_y)
            # for each stopper
            for s_x, s_y in self.stoppers:
                # if ball stops at this stopper
                if is_after(ball_x, ball_y, s_x, s_y):
                    # update position to be one before stopper
                    n_x, n_y = update_pos(s_x, s_y)
                    # and update best position
                    new_x, new_y = set_max(n_x, n_y, new_x, new_y)
            # new_x, new_y will be best position for this ball if only stoppers existed
            # for each ball we already placed
            for other_x, other_y in new_balls:
                # if ball stops at this ball
                if is_after(ball_x, ball_y, other_x, other_y):
                    # update position to be one before ball
                    n_x, n_y = update_pos(other_x, other_y)
                    # and update best position
                    new_x, new_y = set_max(n_x, n_y, new_x, new_y)
            # best position will be the position of the ball after rolling
            new_balls.append((new_x, new_y))
        return new_balls

    def roll_all(self, balls: list[tuple[int, int]], roll_index: int):
        # if we have seen this roll before
        if tuple(balls) in self.dp:
            # return the balls after the roll and the last seen index
            return self.dp[tuple(balls)]
        # copy the key
        key = balls.copy()
        # sort the balls in order
        # row then column ascending
        balls.sort(key=lambda x: x[0] + x[1] * self.columns)
        # and roll up
        balls = self.roll(balls, 0, Direction.UP)
        # sort the balls in order
        # column then row ascending
        balls.sort(key=lambda x: x[1] + x[0] * self.rows)
        balls = self.roll(balls, 0, Direction.LEFT)
        # sort the balls in order
        # row then column descending
        balls.sort(key=lambda x: x[0] +(self.rows - x[1]) * self.columns )
        balls = self.roll(balls, self.rows-1, Direction.DOWN)
        # sort the balls in order
        # column then row descending
        balls.sort(key=lambda x: x[1] + (self.columns - x[0])*self.rows)
        balls = self.roll(balls, self.columns-1, Direction.RIGHT)
        # save the balls and current roll index
        self.dp[tuple(key)] = (balls, roll_index)
        # and return the result
        return balls, -1
    
    def count_y(self, balls: list[tuple[int, int]]):
        return sum(self.rows - y for _, y in balls)

def main():
    with open(os.path.join(sys.path[0],"example.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    
    balls = []
    stoppers = []
    # find all stoppers and balls
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                stoppers.append((x, y))
            elif c == "O":
                balls.append((x, y))
    rows = len(lines)
    columns = len(lines[0])
    
    # create cycle class
    roller = Roller(stoppers, rows, columns)
    # perform rolling of Up, Left, Down, Right
    for i in range(1_000_000_000):
        print(f"roll {i}")
        balls, recurrent = roller.roll_all(balls, i)
        # if we have seen the roll before
        # future rolls will repeat
        if recurrent != -1:
            print(f"recurrent at cycle {i}, starting from {recurrent}")
            # calculate the length of the cycle
            loop = i - recurrent
            # calculate remaining rolls after last occurrence of this roll
            a = (1_000_000_000 - i) % loop
            print(f"performing {a-1} additional rolls")
            for x in range(a-1):
                print(f"roll {x}")
                balls, _ = roller.roll_all(balls, i)
            break
    print(roller.count_y(balls))
    
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
