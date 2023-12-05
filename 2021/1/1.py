import os, sys
input = open(os.path.join(sys.path[0], 'input'), 'r')
lines = input.readlines()

depth = 0
forward = 0
aim = 0

for line in lines:
  line = line.strip()
  if line.startswith("forward"):
    forward += int(line[8:])
    depth += aim * int(line[8:])
  elif line.startswith("down"):
    aim += int(line[5:])
  elif line.startswith("up"):
    aim -= int(line[3:])
print("depth ", depth)
print("forward ", forward)
print ("aim ", aim)
print(depth * forward)