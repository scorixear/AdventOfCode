import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

heightMap = []

for line in lines:
  row = []
  for number in line.strip():
    row.append(int(number))
  heightMap.append(row)

lowestPoints = []

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
    lowestPoints.append([i,j,heightMap[i][j]])


def findBiggerNeighbours(i, j, number):
  returnValue = []
  if i > 0 and heightMap[i-1][j] != 9 and heightMap[i-1][j] > number:
    returnValue.append([i-1, j, heightMap[i-1][j]])
  if j > 0 and heightMap[i][j-1] != 9 and heightMap[i][j-1] > number:
    returnValue.append([i, j-1, heightMap[i][j-1]])
  if i + 1 < len(heightMap) and heightMap[i+1][j] != 9 and heightMap[i+1][j] > number:
    returnValue.append([i+1, j, heightMap[i+1][j]])
  if j + 1 < len(heightMap[i]) and heightMap[i][j+1] != 9 and heightMap[i][j+1] > number:
    returnValue.append([i, j+1, heightMap[i][j+1]])
  return returnValue

def recursiveFind(i, j, number):
  neighBours = findBiggerNeighbours(i, j, number)
  returnValue = neighBours.copy()
  for neighBour in neighBours:
    returnValue.extend(recursiveFind(neighBour[0], neighBour[1], neighBour[2]))
    
  return returnValue

finalList = []

for point in lowestPoints:
  neighBours = recursiveFind(point[0], point[1], point[2])
  newNeighbours = []
  for neighBour in neighBours:
    if next((i for i in newNeighbours if i[0] == neighBour[0] and i[1] == neighBour[1]), None) is None:
      newNeighbours.append(neighBour)
  finalList.append(len(newNeighbours)+1)


firstMax = max(finalList)
finalList.remove(firstMax)
secondMax = max(finalList)
finalList.remove(secondMax)
print(firstMax * secondMax * max(finalList))
    