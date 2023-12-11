import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
# initialize empty columns and rows
    empty_rows = set(list(range(len(lines))))
    empty_columns = set(list(range(len(lines[0]))))
    
    # remove non-empty columns
    for y, row in enumerate(lines):
        # for each cell in that row
        for x, cell in enumerate(row):
            # if the cell is not empty, remove the column from the empty columns
            if cell == "#":
                empty_columns.discard(x)
                empty_rows.discard(y)
    
    # find all galaxies
    galaxies: list[tuple[int, int]] = []
    expansion_size = 1_000_000
    current_additional_y = 0
    for y, row in enumerate(lines):
        if y in empty_rows:
            current_additional_y += 1
            continue
        current_additional_x = 0
        for x, cell in enumerate(row):
            if x in empty_columns:
                current_additional_x += 1
                continue
            if cell == "#":
                galaxies.append((x + current_additional_x * (expansion_size-1) , y + current_additional_y * (expansion_size-1)))
    
    total_distance = 0
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            x, y = galaxies[i]
            x2, y2 = galaxies[j]
            total_distance += abs(x2-x) + abs(y2-y)
    print(total_distance)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
