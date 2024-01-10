# Day 3: Gear Hell
And there we go, day three and the grid problems are back.
This didn't take long. While the puzzle isn't hard so to speak, it can definitly lead you into wrong corners.

We are given a grid of numbers and symbols. Each number is written horizontally and any other cell can be empty (denoted by a ".") or a symbol.

# Part 1
Given the described grid above, find all numbers on that grid, that have at least one symbol touching.

This problem can be approached in two ways: find all symbols, then find all numbers around that symbol.
Or find all numbers, than find all symbols around that number.

The one key problem with finding all symbols first is potential duplicates, that need to be sorted out.
And also, the growing of numbers, as a 3 digit number could be touching a symbol only in one spot, but must be read in as a whole digit.

Therefore, my approach finds all numbers first.

```python
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
```

As seen here, I keep a running variable, that stores all the seen digits of a number so far.
When iterating over a line, seeing a digit means we either extend the current number of create a new one.
The moment, we see a digit, we need to check the 3x3 grid around it for symbols. If there is a symbol, we mark the current number as valid.

When reading in a non-digit character, the currently stored number is finished and if we saw a symbol in the process before, we can add that read in digit to the result.

# Part 2
Part 2 introduces more rules as to which number is considered valid.
We now only consider numbers, that are surround by a gear symbol ("*"). Additionally, a star symbol is only considered a gear symbol, if only two numbers are touching it.

The general structure of the code is the same. We iterate over each line, finding each number and checking the 3x3 grid around it for symbols. 

Differently now, we save the found symbols around each number and after reading in a number fully (by line end or reading in a non-digit character) we check if any of the symbols is a star.

If it is a star, we save this number for this star.
After reading in all numbers, we iterate over each star symbol and check if it has exactly two numbers adjacent.

```python
        # symbols recorded around the digit
        # symbols are recorded as a tuple of (symbol, x, y)
        # I use a set to avoid duplicate entries (because multiple digits can be around the same symbol)
        adjacent_symbols = set()
        # for each character in the line
        for j, c in enumerate(line):
            ... digit reading above ...
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
    for _, values in gears.items():
        # if the gear has exactly two values around it
        if len(values) == 2:
            # add the product of the two values to the result
            result += values[0] * values[1]
    print(result)
```