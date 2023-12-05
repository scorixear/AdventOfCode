import os, sys
with open(os.path.join(sys.path[0], "input"), "r", encoding="utf-8") as f:
    lines = f.read().splitlines(keepends=False)
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
