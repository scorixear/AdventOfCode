from functools import cmp_to_key
import os, sys
import time



def find_next_vertical(x, y, vertical_bars):
    for vert in vertical_bars:
        if vert[0] >= x and vert[1] <= y < vert[2]:
            return vert
    return None

def find_next_horizontal(x, y, horizontal_bars):
    for hori in horizontal_bars:
        if hori[1] > y:
            return None
        if hori[1] == y and hori[0] >= x:
            return hori
    return None

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    # local variable to create region ranges
    position = (0, 0)
    # for iterating through all rows and columns
    max_x, min_x = 0, 0
    max_y, min_y = 0, 0
    # list of vertical and horizontal regions
    vertical_bars = []
    horizontal_bars = []
    for line in lines:
        _, _, instructions = line.split()
        instructions = instructions[2: -1]
        length = instructions[:-1]
        direction = instructions[-1]
        length = int(length, base=16)
        # up
        if direction == "3":
            # add vertical region spanning from current position - length to current position
            # third value is exclusive end of the range
            vertical_bars.append((position[0], position[1] - length, position[1]+1))
            position = (position[0], position[1] - length)
        # down
        elif direction == "1":
            # add vertical region spanning from current position to current position + length
            # third value is exclusive end of the range
            vertical_bars.append((position[0], position[1], position[1] + length + 1))
            position = (position[0], position[1] + length)
        # left
        elif direction == "2":
            # add horizontal region spanning from current position - length to current position
            # third value is exclusive end of the range
            horizontal_bars.append((position[0]-length, position[1], position[0]+1))
            position = (position[0] - length, position[1])
        # right
        elif direction == "0":
            # add horizontal region spanning from current position to current position + length
            # third value is exclusive end of the range
            horizontal_bars.append((position[0], position[1], position[0] + length + 1))
            position = (position[0] + length, position[1])
        # update max and min values
        if position[0] > max_x:
            max_x = position[0]
        elif position[0] < min_x:
            min_x = position[0]
        if position[1] > max_y:
            max_y = position[1]
        elif position[1] < min_y:
            min_y = position[1]
    
    # if the last vertical bar is on the same vertical line as the first vertical bar
    if vertical_bars[0][0] == vertical_bars[-1][0]:
        # and they are both touching ends, they merge
        if vertical_bars[0][1] == vertical_bars[-1][2]:
            vertical_bars[0] = (vertical_bars[0][0], vertical_bars[-1][1], vertical_bars[0][2])
            vertical_bars.pop()
        elif vertical_bars[0][2] == vertical_bars[-1][1]:
            vertical_bars[0] = (vertical_bars[0][0], vertical_bars[0][1], vertical_bars[-1][2])
            vertical_bars.pop()
    # else if the last horizontal bar is on the same horizontal line as the first horizontal bar
    elif horizontal_bars[0][1] == horizontal_bars[-1][1]:
        # and they are both touching ends, they merge
        if horizontal_bars[0][0] == horizontal_bars[-1][2]:
            horizontal_bars[0] = (horizontal_bars[-1][0], horizontal_bars[0][1], horizontal_bars[0][2])
            horizontal_bars.pop()
        elif horizontal_bars[0][2] == horizontal_bars[-1][0]:
            horizontal_bars[0] = (horizontal_bars[0][0], horizontal_bars[0][1], horizontal_bars[-1][2])
            horizontal_bars.pop()

    # sort vertical bars by x coordinate and then by y coordinate
    # when searching for vertical bars that are next to current position
    # we want to find the one with the smallest x coordinate first
    vertical_bars.sort(key=cmp_to_key(lambda a, b:  a[1] - b[1] if a[0] == b[0] else a[0] - b[0]))
    # sort horizontal bars by y coordinate and then by x coordinate
    # when searching for horizontal bars that are next to current position
    # we can skip future horizontal bars if they are above current position
    horizontal_bars.sort(key=cmp_to_key(lambda a, b:  a[0] - b[0] if a[1] == b[1] else a[1] - b[1]))
    
    # counter for the size of the region
    region = 0
    # for each row
    for y  in range(min_y, max_y+1):
        # debug output, as this takes a while
        if (y - min_y) % 100000 == 0:
            print(f"{y}/{max_y}")
        # start at the leftmost x coordinate
        x = min_x
        # flag for if we are in a region
        in_region = False
        # iterate over each x coordinate
        while x <= max_x:
            # find next vertical bar, that is right to the current position
            vert = find_next_vertical(x, y, vertical_bars)
            
            # if no vertical bar is present, no horizontal bar is present
            # we reached end of the line
            if not vert:
                break
            # find next horizontal bar that is right to the current position
            # will start at the end or start of a vertical bar
            hori = find_next_horizontal(x, y, horizontal_bars)
            
            # if no horizontal bar is present or vertical bar is before horizontal bar
            if not hori or vert[0] < hori[0]:
                if in_region:
                    # count the distance between current position and vertical bar
                    region += vert[0] - x
                # and count the vertical bar
                region += 1
                # increase the x coordinate to the end of the vertical bar
                x = vert[0] + 1
                # and swap regions
                in_region = not in_region
            # else both vertical and horizontal bars will be on the same x coordinate
            else:
                # is the vertical bar down facing
                downfacing =  y == vert[1]

                if in_region:
                    # count the distance between current position and vertical bar
                    region += hori[0] - x
                # update x to the end of the horizontal bar
                x = hori[2]
                # and update region size
                region += hori[2] - hori[0]
                # find vertical bar at the end of the horizontal bar
                vert = find_next_vertical(x-1, y, vertical_bars)
                # if vertical bar is down facing and last vertical bar was up facing
                # we swap regions
                if y == vert[1] and not downfacing:
                    in_region = not in_region
                # if vertical bar is up facing and last vertical bar was down facing
                # we swap regions
                elif y == vert[2]-1 and downfacing:
                    in_region = not in_region
    print(region)
            
                
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
