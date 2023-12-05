import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    result = 0
    
    # for each line
    for i, line in enumerate(lines):
        # current number read in
        current_number = ""
        # if digit is surrounded by at least one symbol
        add_digit = False
        
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
                            # and we mark this currently read digit as valid
                            add_digit = True
            # if the current digit is finished reading in (read in a symbol or a dot)
            # and it is valid (has seen at least one symbol)
            # and the current read in digit is not empty (to skip unneeded reassignments)
            elif add_digit and current_number != "":
                # add the digit to the result
                result += int(current_number)
                # and reset the flags
                add_digit = False
                current_number = ""
            # if the current digit is finished reading in (read in a symbol or a dot)
            # but it is not valid (has not seen any symbols)
            else:
                # reset the flags
                add_digit = False
                current_number = ""
        # if the line is finished with a digit
        # the above loop will not add it to the result
        # therefore we check here if the current digit is valid
        # and add it to the result
        if add_digit and current_number != "":
            result += int(current_number)
            # flags are not reset as they are at the beginning of the loop
    print(result)