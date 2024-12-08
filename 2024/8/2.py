import os, sys
import time
import math

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    plane = [list(line) for line in lines]
    width = len(plane[0])
    height = len(plane)
    
    antennas: dict[str, list[tuple[int, int]]] = {}
    for y in range(height):
        for x in range(width):
            if plane[y][x] != ".":
                if plane[y][x] in antennas:
                    antennas[plane[y][x]].append((x, y))
                else:
                    antennas[plane[y][x]] = [(x, y)]
    found: set[tuple[int, int]] = set()
    for ant in antennas.values():
        for i in range(0, len(ant)-1):
            for j in range(i+1, len(ant)):
                new_antinodes = find_antinodes(ant[i], ant[j], width, height)
                for antinode in new_antinodes:
                    if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                        found.add(antinode)
    print(len(found))

def find_antinodes(ant1: tuple[int, int], ant2: tuple[int, int], width: int, height: int) -> set[tuple[int, int]]:
    dist = (ant1[0] - ant2[0], ant1[1] - ant2[1])
    gcd = math.gcd(dist[0], dist[1])
    normalized = (dist[0] // gcd, dist[1] // gcd)
    
    coords: set[tuple[int, int]] = set([ant1, ant2])
    # step in the direction of vector normalized
    curr_coords = (ant1[0], ant1[1])
    while True:
        curr_coords = (curr_coords[0] + dist[0], curr_coords[1] + dist[1])
        if curr_coords[0] < 0 or curr_coords[0] >= width or curr_coords[1] < 0 or curr_coords[1] >= height:
            break
        # if (curr_coords[0], curr_coords[1]) == ant1 or (curr_coords[0], curr_coords[1]) == ant2:
        #     continue
        coords.add(curr_coords)
    # step in the opposite direction of vector normalized
    curr_coords = (ant1[0], ant1[1])
    while True:
        curr_coords = (curr_coords[0] - dist[0], curr_coords[1] - dist[1])
        if curr_coords[0] < 0 or curr_coords[0] >= width or curr_coords[1] < 0 or curr_coords[1] >= height:
            break
        # if (curr_coords[0], curr_coords[1]) == ant1 or (curr_coords[0], curr_coords[1]) == ant2:
        #     continue
        coords.add(curr_coords)
    
    
    return coords

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
