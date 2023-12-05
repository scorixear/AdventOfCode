"""provides path joining functions annd module joining"""
import os
import sys
import time

INPUT_FILE="input"

class node:
  connections: list["node"]
  def __init__(self,x: int,y: int,elevation: int):
    self.x = x
    self.y = y
    self.elevation = elevation
    self.connections = []
  def add_neighbour(self, other: "node"):
    if other.elevation - self.elevation <= 1:
      self.connections.append(other)
  def find_connections(self, grid: list[list["node"]]):
    # upper edge
    if self.y > 0:
      # x00
      #if self.x > 0:
      #  self.add_neighbour(grid[self.y-1][self.x-1])
      # 0x0
      self.add_neighbour(grid[self.y-1][self.x])
      # 00x
      #if self.x < len(grid[self.y-1])-1:
      #  self.add_neighbour(grid[self.y-1][self.x+1])
    # x.0
    if self.x > 0:
      self.add_neighbour(grid[self.y][self.x-1])
    # 0.x
    if self.x < len(grid[self.y])-1:
      self.add_neighbour(grid[self.y][self.x+1])
    # lower edge
    if self.y < len(grid)-1:
      # x00
      #if self.x > 0:
      #  self.add_neighbour(grid[self.y+1][self.x-1])
      # 0x0
      self.add_neighbour(grid[self.y+1][self.x])
      # 00x
      #if self.x < len(grid[self.y+1])-1:
      #  self.add_neighbour(grid[self.y+1][self.x+1])
      
def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  grid: list[list[node]] = [[] for _ in range(len(lines))]
  startNode = None
  endNode = None
  for y,line in enumerate(lines):
    #print(line.strip())
    for x,char in enumerate(line.strip()):
      newNode = node(x,y,0)
      if char == "S":
        newNode.elevation = 1
        startNode = newNode
      elif char == "E":
        newNode.elevation = 26
        endNode = newNode
      else:
        newNode.elevation = ord(char)-96
      grid[y].append(newNode)
  for rows in grid:
    for cell in rows:
      cell.find_connections(grid)
  if startNode is not None and endNode is not None:
    intermitten = dijkstra(grid, startNode, endNode)
    path = find_path(endNode, intermitten)

    print(len(path)-1)
    #print_path(grid, path)

def print_path(grid: list[list[node]], path: list[node]):
  lines = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
  for index, node in enumerate(path):
    #print(f"x: {node.x}, y: {node.y}")
    if index == 0:
      lines[node.y][node.x] = "S"
    elif index == len(path)-1:
      lines[node.y][node.x] = "E"
    else:
      next = path[index+1]
      replaceChar = ""
      if node.x == next.x:
        if node.y < next.y:
          replaceChar = "v"
        else:
          replaceChar = "^"
      elif node.x < next.x:
        replaceChar = ">"
      else:
        replaceChar = "<"
      lines[node.y][node.x] = replaceChar
  for line in lines:
    print("".join(line))

def dijkstra(graph: list[list[node]], startNode: node, targetNode: node):
  distances: dict[node, int] = {}
  previous: dict[node, node] = {}
  Q: list[node] = []
  initialise(graph, startNode, distances, Q)
  while len(Q) > 0:
    u: node = find_smallest(Q, distances)
    Q.remove(u)
    if u == targetNode:
      break
    for v in u.connections:
      if v in Q:
        distance_update(u,v,distances,previous)
  return previous

def initialise(graph: list[list[node]], startNode: node, distances: dict[node, int], Q: list[node]):
  for y in graph:
    for x in y:
      Q.append(x)
      distances[x] = 100_000
  distances[startNode] = 0

def distance_update(u: node, v: node, distances: dict[node, int], previous: dict[node, node]):
  alternative = distances[u] + 1
  if alternative < distances[v]:
    distances[v] = alternative
    previous[v]= u

def find_smallest(Q: list[node], distances: dict[node, int]):
  smallestNode = Q[0]
  smallestWeight = distances[smallestNode]
  for n in Q:
    if distances[n] < smallestWeight:
      smallestWeight = distances[n]
      smallestNode = n
  return smallestNode  

def find_path(target: node, previous: dict[node, node]):
  path = [target]
  u = target
  while u in previous:
    u = previous[u]
    path.insert(0, u)
  return path

if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")