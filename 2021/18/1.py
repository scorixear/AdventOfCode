import os, sys
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

class Node:
  def __init__(self):
    self.leftNode: "Node | None" = None
    self.rightNode: "Node | None" = None
    self.leftValue: "int | None" = None
    self.rightValue: "int | None" = None
    self.parent: "Node | None" = None
  def add(self, other: "Node"):
    parent = Node()
    parent.leftNode = self
    parent.rightNode = other
    self.parent = parent
    other.parent = parent
    return parent
  def setLeft(self, left: "Node | int"):
    if isinstance(left, Node):
      self.leftNode = left
      self.leftNode.parent = self
      self.leftValue = None
    else:
      self.leftValue = left
      self.leftNode = None
  def setRight(self, right: "Node | int"):
    if isinstance(right, Node):
      self.rightNode = right
      self.rightNode.parent = self
      self.rightValue = None
    else:
      self.rightValue = right
      self.rightNode = None
  def findParentWithLeft(self):
    if self.parent is not None and self.parent.leftNode is not self:
      return self.parent
    if self.parent is not None:
      return self.parent.findParentWithLeft()
    return None
  def findParentWithRight(self):
    if self.parent is not None and self.parent.rightNode is not self:
      return self.parent
    if self.parent is not None:
      return self.parent.findParentWithRight()
    return None
  def findMostRight(self):
    if self.rightNode is None:
      return (self, 1)
    return self.rightNode.findMostRight()
  def findMostLeft(self):
    if self.leftNode is None:
      return (self, 0)
    return self.leftNode.findMostLeft()
  def findNextLeft(self):
    leftParent = self.findParentWithLeft()
    if leftParent is None:
      return (None,  None)
    if leftParent.leftNode is None:
      return (leftParent, 0)
    return leftParent.leftNode.findMostRight()
  def findNextRight(self):
    rightParent = self.findParentWithRight()
    if rightParent is None:
      return (None,  None)
    if rightParent.rightNode is None:
      return (rightParent, 1)
    return rightParent.rightNode.findMostLeft()
  def getDepth(self):
    if self.parent is None:
      return 0
    return self.parent.getDepth() + 1
  def __str__(self):
    return f"[{self.leftValue.__str__() if self.leftNode is None else self.leftNode.__str__()},{self.rightValue.__str__() if self.rightNode is None else self.rightNode.__str__()}]"
  def __repr__(self):
    return self.__str__()
  def explode(self):
    if self.getDepth() >= 4:
      if self.leftValue is not None and self.rightValue is not None:
        parent, side = self.findNextLeft()
        if parent is not None:
          if side:
            parent.rightValue += self.leftValue
          else:
            parent.leftValue += self.leftValue
        parent, side = self.findNextRight()
        if parent is not None:
          if side:
            parent.rightValue += self.rightValue
          else:
            parent.leftValue += self.rightValue
        if self.parent.leftNode is self:
          self.parent.leftNode = None
          self.parent.leftValue = 0
        else:
          self.parent.rightNode = None
          self.parent.rightValue = 0
        return True
      exploded = False
      if self.leftNode is not None:
        exploded = self.leftNode.explode()
      if exploded is False and self.rightNode is not None:
        return self.rightNode.explode()
      return exploded
    else:
      exploded = False
      if self.leftNode is not None:
        exploded = self.leftNode.explode()
      if exploded is False and self.rightNode is not None:
        return self.rightNode.explode()
      return exploded
  def split(self):
    if self.leftValue is not None:
      if self.leftValue >= 10:
        newNode = Node()
        newNode.leftValue = self.leftValue // 2
        newNode.rightValue = self.leftValue - (self.leftValue // 2)
        self.setLeft(newNode)
        return True
    splitted = False
    if self.leftNode is not None:
      splitted = self.leftNode.split()
    if splitted is False:
      if self.rightValue is not None:
        if self.rightValue >= 10:
          newNode = Node()
          newNode.leftValue = self.rightValue // 2
          newNode.rightValue = self.rightValue - (self.rightValue//2)
          self.setRight(newNode)
          return True
      if self.rightNode is not None:
        return self.rightNode.split()
    return splitted
  def magnitude(self):
    leftMagnitude = 0
    rightMagnitude = 0
    if self.leftNode is None:
      leftMagnitude = 3*self.leftValue
    else:
      leftMagnitude = 3*self.leftNode.magnitude()
    if self.rightNode is None:
      rightMagnitude = 2*self.rightValue
    else:
      rightMagnitude = 2*self.rightNode.magnitude()
    return leftMagnitude+rightMagnitude



def findSplit(string: str):
  counter = 0
  currentStr = string
  indexPosition = 0
  if currentStr.startswith("[") is False:
    split = currentStr.split(",")
    return len(split[0])
  for char in string:
    if char == "[":
      counter += 1
    elif char == "]":
      counter -= 1
    indexPosition += 1
    if counter == 0:
      return indexPosition
    
  return None

def parseNode(string: str) -> "Node":
  content = string[1:-1]
  splitIndex = findSplit(content)
  leftStr = content[:splitIndex]
  rightStr = content[splitIndex+1:]
  node = Node()
  if leftStr.startswith("["):
    left = parseNode(leftStr)
  else:
    left = int(leftStr)
  if rightStr.startswith("["):
    right = parseNode(rightStr)
  else:
    right = int(rightStr)
  node.setLeft(left)
  node.setRight(right)
  return node
  

root = None
for line in lines:
  if root is None:
    root = parseNode(line.strip())
  else:
    root = root.add(parseNode(line.strip()))
    while True:
      if root.explode() is False and root.split() is False:
        break;
print(root)
print(root.magnitude())