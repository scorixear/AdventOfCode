import os, sys
input = open(os.path.join(sys.path[0], 'input.txt'), 'r')
lines = input.readlines()

count = -1
lastNumber = -1
for line in lines:
  if(lastNumber < int(line.strip())):
    count += 1
  lastNumber = int(line.strip())

print(count)
