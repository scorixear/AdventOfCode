import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

heightMap = []

for line in lines:
  row = []
  for number in line.strip():
    row.append(int(number))
  heightMap.append(row)

sum = 0

for i in range(len(heightMap)):
  for j in range(len(heightMap[i])):
    if i > 0 and heightMap[i-1][j] <= heightMap[i][j]:
      continue
    if j > 0 and heightMap[i][j-1] <= heightMap[i][j]:
      continue
    if i + 1 < len(heightMap) and heightMap[i+1][j] <= heightMap[i][j]:
      continue
    if j + 1 < len(heightMap[i]) and heightMap[i][j+1] <= heightMap[i][j]:
      continue
    sum += heightMap[i][j]+1
print(sum)
    