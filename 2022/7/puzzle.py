"""provides path joining functions annd module joining"""
import os
import sys
import time
import functools
from typing import Optional

INPUT_FILE="input"

class Node:
  def __init__(self, name: str, parent: Optional["Node"]):
    self.name: str = name
    self.nodes: list[Node] = []
    self.size: int = 0
    self.parent: Optional["Node"] = parent
  def is_directory(self) -> bool:
    return self.size==0
  def get_directory(self, name) -> Optional["Node"]:
    for node in self.nodes:
      if node.name == name and node.is_directory():
        return node
    return None
  def __repr__(self) -> str:
   return f"{self.name} ({'dir' if self.size==0 else 'file, '+str(self.size)})"
  def print(self, indent = "") -> None:
    print(indent+self.__repr__())
    for node in self.nodes:
      node.print(indent + "   ")

  @functools.cache
  def get_size(self) -> int:
    if self.size == 0:
      sum = 0
      for node in self.nodes:
        sum += node.get_size()
      return sum
    return self.size
  def get_directories(self) -> list["Node"]:
    if self.size != 0:
      return []
    directories = []
    for node in self.nodes:
      if node.is_directory():
        directories.append(node)
        directories.extend(node.get_directories())
    return directories


def solve1(root: "Node"):
  dirs = root.get_directories()
  sum = 0
  for folder in dirs:
    size = folder.get_size()
    if size <= 100_000:
      sum += size
  print(f"Total Sum: {sum}\nTotal Folders: {len(dirs)}")

def solve2(root: "Node"):
  used_space = root.get_size()
  free_space = 70_000_000 - used_space
  missing_space = 30_000_000 - free_space
  folders = root.get_directories()
  smallest = used_space
  for folder in folders:
    if folder.get_size() < smallest and folder.get_size() >= missing_space:
      smallest = folder.get_size()
  print(f"Used Space: {used_space}\nFree Space: {free_space}\nMising Space: {missing_space}\nSmallest Directory: {smallest}")

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  root = Node("/", None)
  currentNode: Optional["Node"] = None
  for line in lines:
    if line.startswith("$"):
      if line.startswith("$ cd "):
        if line.strip()[5:] == "/":
          currentNode = root
          continue
        if currentNode is not None:
          if line.strip()[5:] == "..":
            currentNode = currentNode.parent
            continue
          selectedDir = currentNode.get_directory(line.strip()[5:])
          if selectedDir is not None:
            currentNode = selectedDir
    elif currentNode is not None:
      if line.startswith("dir "):
        dirNode = Node(line.strip()[4:], currentNode)
        currentNode.nodes.append(dirNode)
      else:
        size = int(line.strip().split(" ")[0])
        name = line.strip().split(" ")[1]
        fileNode = Node(name, currentNode)
        fileNode.size = size
        currentNode.nodes.append(fileNode)
  #root.print()
  solve2(root)
 





if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")