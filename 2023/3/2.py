from collections import defaultdict
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    # this will hold the coordinates of the gears
    # and their values around them
    gears: dict[tuple[int, int], list[int]] = defaultdict(list)
    # for each line
    for i, line in enumerate(lines):
        # current number read in
        current_number = ""
        # symbols recorded around the digit
        # symbols are recorded as a tuple of (symbol, x, y)
        # I use a set to avoid duplicate entries (because multiple digits can be around the same symbol)
        adjacent_symbols = set()

        # for each character in the line
        for j, c in enumerate(line):
            # if character is a digit
            if c.isdigit():
                # append to current number
                current_number += c
                # for each character in the 3x3 grid around the digit
                for x in range(max(0,i-1), min(len(lines), i+2)):
                    for y in range(max(0, j-1), min(len(line), j+2)):
                        # exclude the digit itself
                        if x == i and y == j:
                            continue
                        # if the character is not a digit and not a dot, it is a symbol
                        if lines[x][y] != "." and not lines[x][y].isdigit():
                            # and we add it to the set of adjacent symbols
                            adjacent_symbols.add((lines[x][y], x, y))
            # if we read in a symbol or a dot
            # the current number is finished reading in
            # and if it even has symbols around it
            # and a number is read in at all (to avoid unneeded reassignments)
            elif len(adjacent_symbols) != 0 and current_number != "":
                # for each symbol around the digit
                for symbol, x, y in adjacent_symbols:
                    # if the symbol is a gear
                    if symbol == "*":
                        # add the current number to the list of values around the gear
                        gears[(x,y)].append(int(current_number))
                # reset the flags
                adjacent_symbols = set()
                current_number = ""
            # if we read in a symbol or a dot
            # the current number is finished reading in
            # but it has no symbols around it
            else:
                # reset the flags
                adjacent_symbols = set()
                current_number = ""
        # if the line is finished with a digit
        # the above loop will not add it to the result
        # therefore we check here if the current number has symbols around it
        # and if it even has a number read in (to avoid unneeded reassignments)
        if len(adjacent_symbols) != 0 and current_number != "":
            # for each symbol around the digit
            for symbol, x, y in adjacent_symbols:
                # if the symbol is a gear
                if symbol == "*":
                    # add the current number to the list of values around the gear
                    gears[(x,y)].append(int(current_number))
    result = 0
    # for each gear
    for key, values in gears.items():
        # if the gear has exactly two values around it
        if len(values) == 2:
            # add the product of the two values to the result
            result += values[0] * values[1]
    print(result)