import os, sys
input = open(os.path.join(sys.path[0], 'input.txt'), 'r')
lines = input.readlines()

count = -1
lastSum = -1
for i in range(len(lines) - 2):
  sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
  if(lastSum < sum):
    count += 1
  lastSum = sum
print(count)