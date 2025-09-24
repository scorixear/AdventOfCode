import time
from dijkstra import Dijkstra
def main():
    num = 1364
    start = (1,1)
    end=(31,39)
    solver = Dijkstra(lambda x: get_neighbours(x, num), lambda a,b:1, 0)
    solver.find_path(start, end)
    print(solver.get_cost(end))

def get_neighbours(node, num):
    x,y = node
    candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    neighbours = []
    for cx,cy in candidates:
        val = cx*cx + 3*cx + 2*cx*cy + cy + cy*cy + num
        if cx >= 0 and cy >= 0 and bin(val).count("1") % 2 == 0:
            neighbours.append((cx,cy))
    return neighbours
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
