import os, sys
import time
import networkx as nx


def tadd(a, b):
    return (a[0]+b[0], a[1]+b[1])

def main():
    with open(os.path.join(sys.path[0],"example.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    # create a set of coordinates, that are allowed to be walked on
    grid = {(x,y) for y,line in enumerate(lines) for x,c in enumerate(line) if c != "#"}
    
    # start node
    S = (1, 0)
    # end node
    E  = (len(lines[0])-2, len(lines)-1)
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # set of positions already visited
    visited = {S}
    # stack of directions that need to be observed
    # filled with all possible directions from the start node
    stack = []
    for i, direction in enumerate(directions):
        new_pos = tadd(S, direction)
        if new_pos in grid:
            stack.append((S, i))
    
    graph = nx.Graph()
    while stack:
        # get the next direction
        start, direction = stack.pop()
        # get the next position after this direction
        previous = start
        current = tadd(start, directions[direction])
        length = 1
        # and add the next position to the visited set
        visited.add(current)
        # get the directions that can be reached from the current position
        new_dirs = []
        for i, dir in enumerate(directions):
            new_pos  = tadd(current, dir)
            if new_pos in grid:
                new_dirs.append((i, new_pos in visited))
        # as long as this is not a junction
        while len(new_dirs) == 2:
            # get the next direction that is not the direction we came from
            direction = None
            for d_index, _ in new_dirs:
                if previous != tadd(current, directions[d_index]):
                    direction = d_index
                    break
            # get next position
            previous = current
            current = tadd(current, directions[direction])
            length += 1
            # and find all directions again
            new_dirs = []
            for i, dir in enumerate(directions):
                new_pos  = tadd(current, dir)
                if new_pos in grid:
                    new_dirs.append((i, new_pos in visited))
        # we found a junction at the current node
        # so we add an edge between start and current
        graph.add_edge(start, current, cost=length)
        
        # add all directions you can walk from the current position
        # exclude position we came from
        for d_index, vis in new_dirs:
            if not vis:
                stack.append((current, d_index))
    # get all simple paths from start to end
    # and the maximum path weight for all paths
    res = max(nx.path_weight(graph, path, "cost") for path in nx.all_simple_paths(graph, S, E))
    print(res)
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
