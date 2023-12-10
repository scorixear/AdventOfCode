import os, sys
import time

def traverse(lines, pos, prev):
    char = lines[pos[1]][pos[0]]
    add_x = 0
    add_y = 0
    # if pipe down
    if char == "|":
        # if prev is above
        if prev[1] < pos[1]:
            # move down
            add_y = 1
        # if prev is below
        else:
            # move up
            add_y = -1
    # if pipe right
    elif char == "-":
        # if prev is left
        if prev[0] < pos[0]:
            # move right
            add_x = 1
        # if prev is right
        else:
            # move left
            add_x = -1
    # if pipe down right
    elif char == "L":
        # if prev is above
        if prev[1] < pos[1]:
            # move right
            add_x = 1
        # if prev is right
        else:
            # move up
            add_y = -1
    # if pipe down left
    elif char == "J":
        # if prev is above
        if prev[1] < pos[1]:
            # move left
            add_x = -1
        # if prev is left
        else:
            # move up
            add_y = -1
    # if pip left down
    elif char == "7":
        # if prev is below
        if prev[1] > pos[1]:
            # move left
            add_x = -1
        # if prev is left
        else:
            # move down
            add_y = 1
    # if pipe right down
    elif char == "F":
        # if prev is below
        if prev[1] > pos[1]:
            # move right
            add_x = 1
        # if prev is right
        else:
            # move down
            add_y = 1
    else:
        raise Exception(f"No loop at position {pos[0]}, {pos[1]}, {char}")
    prev[0] = pos[0]
    prev[1] = pos[1]
    pos[0] += add_x
    pos[1] += add_y
                

def main():
    with open(os.path.join(sys.path[0],"example2.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
     # find start position
    startx, starty = None, None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                startx, starty = x, y
                break
        if startx is not None:
            break
    
    # verify that only two connections exist
    # and find them
    connections = []
    # if position on the left can connect to start
    if lines[starty][startx-1] in "-LF":
        connections.append([startx-1, starty])
    # if position on the right can connect to start
    if lines[starty][startx+1] in "-J7":
        connections.append([startx+1, starty])
    # if position above can connect to start
    if lines[starty-1][startx] in "|7F":
        connections.append([startx, starty-1])
    # if position below can connect to start
    if lines[starty+1][startx] in "|LJ":
        connections.append([startx, starty+1])
    if len(connections) != 2:
        raise Exception(f"Start has {connections} connections")
    
    # get first and second connections and save previous positions
    counter = 1
    first = connections[0]
    prev_first = [startx, starty]
    second = connections[1]
    prev_second = [startx, starty]
    
    # while the first and second connections are not the same
    while first[0] != second[0] or first[1] != second[1]:
        # get next location
        traverse(lines, first, prev_first)
        traverse(lines, second, prev_second)
        # increment counter
        counter += 1
    # when the first and second connections are the same, we hit maximum distance
    print(counter)
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
