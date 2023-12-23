import os, sys
import time
from dijkstra import Dijkstra

def main():
    with open(os.path.join(sys.path[0],"example.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    # read in grid and start and end positions
    grid = [[c for c in line] for line in lines]
    start = (1,0)
    end  = (len(grid[0])-2, len(grid)-1)
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def get_neighbours(current: tuple[int, int], previous: dict[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
        neighbours: list[tuple[int, int]] = []
        cell = grid[current[1]][current[0]]
        # if the current cell is a slope
        if cell not in [".", "#"]:
            # if the next cell after the slope is inside the grid and not the previous cell
            if cell == ">" and current[0] < len(grid[0])-1 and (current[0]+1, current[1]) != previous[current]:
                return [(current[0]+1, current[1])]
            if cell == "<" and current[0] > 0 and (current[0]-1, current[1]) != previous[current]:
                return [(current[0]-1, current[1])]
            if cell == "^" and current[1] > 0 and (current[0], current[1]-1) != previous[current]:
                return [(current[0], current[1]-1)]
            if cell == "v" and current[1] < len(grid)-1 and (current[0], current[1]+1) != previous[current]:
                return [(current[0], current[1]+1)]
            return []
        # if the current cell is not a slope
        for direction in directions:
            neighbour = (current[0]+direction[0], current[1]+direction[1])
            # if the next cell is in the grid and can be walked on and is not the previous cell
            if 0 <= neighbour[0] < len(grid[0]) and 0 <= neighbour[1] < len(grid) and neighbour != previous[current]:
                if grid[neighbour[1]][neighbour[0]] != "#":
                    neighbours.append(neighbour)
        return neighbours
    def get_cost(current: tuple[int, int], neighbour: tuple[int, int]) -> int:
        # reversed dijkstra
        return -1
        
    dijk: Dijkstra[int, tuple[int, int]] = Dijkstra(get_neighbours, get_cost)
    # no early stopping to traverse all paths
    dijk.find_path(start, None)
    print(dijk.get_cost(end))
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
