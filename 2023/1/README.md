# 2023 Day 1: Word Mangel

## General Setup explanation
With Word Mangel, being the first day of the aoc year 2023, it is time to explain the main structure of my code here.

An example python file with no solution looks like this:
```python
import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")


if __name__ == "__main__":
  before = time.perf_counter()
  main()
  print(f"Time: {time.perf_counter() - before:.6f}s")
```

Not perfect, not bad, just usefull.
I like to time my code to see if later improvements actually improve the runtime.
For that I use the built in `time` module. and its `perf_counter()` function.
The `perf_counter()` function returns the current time in seconds as a float and is nanoseconds precise (as I am told), but I only use it to measure milliseconds at best.

When reading in the input, I use the `os` and `sys` modules to get the path to the input file.
As I don't like to run my code from the same directory the python file is located, but generally want my input file to be at the same level as my python file, the `sys` module provides the `sys.path[0]` variable, which is the path to the current directory this python file is located in.

With the `with` statement, I don't have to worry about closing the file, as it is closed automatically when the `with` block is left.
As most of the input files of AoC have some sort of line by line parsing included, I presplit the line in every solution with `lines = text.split("\n")`.
Note that I work wtih LF files and not CRLF files.

# The actual problem 1
We are given a list of strings, each containing digits and non-digit characters.
Our goal, find the first and last digit in each string, and read them as one number.
Then, add all those numbers together.

A pretty straight forward problem for a day one part 1.
My solution aims for single pass. I want to iterate over each line at most once.

```python	
result = 0
for line in lines:
    first, last = None, None
    for c in line:
        if c.isdigit():
            if first is None:
                first = c
            last = c
    result += int(first + last)
print(result)
```

For each line, I preset the first and last digit seen to `None`.
Then, I iterate over each character in the line.
The moment I see a digit, I check if this is the first digit seen. If so, set it.
Otherwise, each digit read in might be the last didit seen in this line.
So constantly overwriting the last counter always savest the last seen digit.

# Part 2
Now, the given lines of characters not only contain digits, but also spelled out digits.
Meaining "one" could be present and could be the first digit seen.
In a line spelled out like this "oneighthree2" the digits "1", "8", "3" and "2" are present.
So the solution would be a "12".

One again, a single pass through is the goal and also greatly simplifies the solution.

```python
result = 0
digits = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for line in lines:
    first, last = None, None
    for i,c in enumerate(line):
        if c.isdigit():
            if first is None:
                first = int(c)
            last = int(c)
        else:
            if i < len(line) - 2 and line[i:i+3] in digits:
                if first is None:
                    first = digits[line[i:i+3]]
                last = digits[line[i:i+3]]
                continue
            if i < len(line) - 3 and line[i:i+4] in digits:
                if first is None:
                    first = digits[line[i:i+4]]
                last = digits[line[i:i+4]]
                continue
            if i < len(line) - 4 and line[i:i+5] in digits:
                if first is None:
                    first = digits[line[i:i+5]]
                last = digits[line[i:i+5]]
                continue
    result += first*10 + last
print(result)
```

Firstly, I used a dictionary to map spelled out digits to their integer representation.
Then, I iterate over each character in the line.
If the character is a digit, this is the same as in part 1. If this is the first digit seen, set the first digit variable, otherwise overwrite the last digit variable.

If the read in character is not a digit, this might be a spelled out digit.
So if there is enough characters left in the line to spell out a 3 character long word (such as "one" or "six"), and if so I check if the given 3 characters are in the dictionary of spelled out words.

The smae check is done for 4 and 5 character long words.
If a spelled out word is found, the first and last digit variables are set accordingly and the loop continues.