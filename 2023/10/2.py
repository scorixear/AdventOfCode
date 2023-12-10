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
    prev[0] = pos[0]
    prev[1] = pos[1]
    pos[0] += add_x
    pos[1] += add_y
                

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
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
    
    # set start pipe
    # if first connection is above start
    if connections[0][0] == startx and connections[0][1] == starty-1:
        # if second connection is left of start
        if connections[1][0] == startx-1:
            start_pipe = "J"
        # if second connection is right of start
        elif connections[1][0] == startx+1:
            start_pipe = "L"
        # if second connection is below start
        else:
            start_pipe = "|"
    # if first connection is below start
    elif connections[0][0] == startx and connections[0][1] == starty+1:
        # if second connection is left of start
        if connections[1][0] == startx-1:
            start_pipe = "7"
        # if second connection is right of start
        elif connections[1][0] == startx+1:
            start_pipe = "F"
        # if second connection is above start
        else:
            start_pipe = "|"
    # if first connection is left of start
    elif connections[0][1] == starty and connections[0][0] == startx-1:
        # if second connection is above start
        if connections[1][1] == starty-1:
            start_pipe = "J"
        # if second connection is below start
        elif connections[1][1] == starty+1:
            start_pipe = "7"
        # if second connection is right of start
        else:
            start_pipe = "-"
    # if first connection is right of start
    elif connections[0][1] == starty and connections[0][0] == startx+1:
        # if second connection is above start
        if connections[1][1] == starty-1:
            start_pipe = "L"
        # if second connection is below start
        elif connections[1][1] == starty+1:
            start_pipe = "F"
        # if second connection is left of start
        else:
            start_pipe = "-"
    # set start pipe character
    lines[starty] = lines[starty][:startx] + start_pipe + lines[starty][startx+1:]
    
    # get first and second connections and save previous positions
    first = connections[0]
    prev_first = [startx, starty]
    second = connections[1]
    prev_second = [startx, starty]
    
    # set of positions of all pipes that are in the loop
    # starting with the start pipe and the two connections
    pipes = set([(startx, starty), (first[0], first[1]), (second[0], second[1])])
    # while the first and second connections are not the same
    while first[0] != second[0] or first[1] != second[1]:
        # get next locations
        traverse(lines, first, prev_first)
        traverse(lines, second, prev_second)
        # add them to the set of pipes
        pipes.add((first[0], first[1]))
        pipes.add((second[0], second[1]))
    
    # switch weather we are in a region or not
    is_region = False
    # count the number of cells in a region
    region_counter = 0
    # keep track of the previous edge if it was an edge pipe (L, F)
    previous_edge = None
    # for every cell in the grid
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            # if the cell is not a pipe of the loop and we are in a region
            if (x,y) not in pipes and is_region:
                region_counter += 1
            # if the cell is a pipe of the loop
            elif (x,y) in pipes:
                # a pipe down always switches the region
                if c == "|":
                    is_region = not is_region
                # a pipe right doesn't affect the region
                elif c == "-":
                    continue
                # a pipe edge pointing to the right
                # will begin a series of 0..n "-" pipes ending with either J or 7
                # we count each L----J or F----7 as non existent
                # and each L----7 or F----J as existent region boundary
                if c in "LF":
                    previous_edge = c
                # a pipe edge pointing to the left
                elif c == "J":
                    # if previous edge wasn't pointing up
                    if previous_edge == "F":
                        # switch region
                        is_region = not is_region
                    previous_edge = None
                # a pipe edge pointing to the right
                elif c == "7":
                    # if previous edge wasn't pointing down
                    if previous_edge == "L":
                        # switch region
                        is_region = not is_region
                    previous_edge = None
                # end switch for pipes
            # end if cell is a pipe
        # end for x in line
    # end for y in lines
    print(region_counter)
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
