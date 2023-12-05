import os, sys
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

crabs = lines[0].split(',')
crabs = [int(item) for item in crabs]

min = min(crabs)
max = max(crabs)

bestFuel = sys.maxsize
bestPosition = -1
for i in range(min, max+1):
  currentFuel = 0
  for crab in crabs:
    difference = abs(i-crab)
    currentFuel += (difference*(difference + 1))/2
  if currentFuel < bestFuel:
    bestFuel = currentFuel
    bestPosition = i

print(bestFuel, bestPosition)
