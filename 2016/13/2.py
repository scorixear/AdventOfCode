import time
def main():
    num = 1364
    start = (1,1)
    visited = set()
    queue = [(0,start)]
    while queue:
        step, current = queue.pop(0)
        if current in visited:
            continue
        if step > 50:
            continue
        visited.add(current)
        for neighbour in get_neighbours(current, num):
            queue.append((step+1, neighbour))
    print(len(visited))

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
