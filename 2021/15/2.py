import os, sys, re, time
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

class Neighbour:
  def __init__(self, targetIndex, weight):
    self.targetIndex = targetIndex
    self.weight = weight;

def getIndices(index):
  return (index // len(grid), index % len(grid))

def getIndex(x, y):
  return (x * len(grid) + y)

def computeShortesPathByDijkstra(startIndex: int):
  numberOfVerticies = len(grid)*len(grid)
  global minimumDistance
  minimumDistance.clear()
  minimumDistance = [float("inf")]*numberOfVerticies
  minimumDistance[startIndex] = 0
  global previousVerticies
  previousVerticies.clear();
  previousVerticies = [-1]*numberOfVerticies
  vertexQueue: "list[tuple[float, int]]" = []
  vertexQueue.append((minimumDistance[startIndex], startIndex));
  while len(vertexQueue) > 0:
    distance, index = vertexQueue[0]
    del vertexQueue[:1]
    neighbours = []
    if index % len(grid) > 0:
      neighbours.append(index-1)
    if index+len(grid)<numberOfVerticies:
      neighbours.append(index + len(grid))
    if index-len(grid) >= 0:
      neighbours.append(index-len(grid))
    if (index + 1)% len(grid) > 0:
      neighbours.append(index +1)
    for neighbour in neighbours:
      targetIndex = neighbour
      pair = getIndices(targetIndex)
      weight = grid[pair[0]][pair[1]]
      currentDistance = distance + weight
      if currentDistance < minimumDistance[targetIndex]:
        try:
          vertexQueue.remove((minimumDistance[targetIndex], targetIndex))
        except ValueError:
          None
        minimumDistance[targetIndex] = currentDistance
        previousVerticies[targetIndex] = index
        vertexQueue.append((minimumDistance[targetIndex], targetIndex))




def getShortestPathTo(index, previousVerticies: "list[int]"):
  path = []
  while index != -1:
    path.insert(0, getIndices(index))
    index = previousVerticies[index]
  return path

tempgrid: "list[list[int]]" = []
for line in lines:
  row = []
  for char in line.strip():
    row.append(int(char))
  tempgrid.append(row)
grid: "list[list[int]]" = []

for i in range(5):
  for oldRow in tempgrid:
    newRow = []
    for j in range(5):
      for cell in oldRow:
        newRow.append(((cell-1)+i+j)%9+1)
    grid.append(newRow)
    # print(newRow)


minimumDistance: "list[float]" = []
previousVerticies: "list[int]" = []

computeShortesPathByDijkstra(0);
print("Distance", minimumDistance[(len(grid))*(len(grid))-1])
path: "list[tuple[int,int]]" = getShortestPathTo((len(grid))*(len(grid))-1, previousVerticies)
print("Path", path)