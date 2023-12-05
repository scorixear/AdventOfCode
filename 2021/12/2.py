import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

class Node:
  def __init__(self, small: bool, name: str):
    self.isSmall: bool = small
    self.Nodes: "list[Node]" = []
    self.Name = name
    self.VisitCounter = 0
  def addNode(self, node: "Node"):
    if node not in self.Nodes:
      self.Nodes.append(node)
  def visit(self):
    self.VisitCounter += 1
  def unVisit(self):
    self.VisitCounter -= 1
  def setVisit(self, number):
    self.VisitCounter = number
  def __eq__(self, other):
    if isinstance(other, Node):
      return other.Name == self.Name
    return NotImplemented
  def __hash__(self) -> int:
      return hash(self.Name)
  def __str__(self) -> str:
      return self.Name
  def __repr__(self) -> str:
      return self.__str__()

Nodes: "list[Node]" = []
startNode = Node(False, "")
endNode = Node(False, "")

for line in lines:
  nodeNames = line.strip().split("-")
  firstNode = Node(nodeNames[0] == nodeNames[0].lower(), nodeNames[0])
  secondNode = Node(nodeNames[1] == nodeNames[1].lower(), nodeNames[1])
  if firstNode not in Nodes:
    if nodeNames[0] == "start":
      startNode = firstNode
    elif nodeNames[0] == "end":
      endNode = firstNode
    Nodes.append(firstNode)
  else:
    firstNode = Nodes[Nodes.index(firstNode)]
  if secondNode not in Nodes:
    if nodeNames[1] == "start":
      startNode = secondNode
    elif nodeNames[1] == "end":
      endNode = secondNode
    Nodes.append(secondNode)
  else:
    secondNode = Nodes[Nodes.index(secondNode)]
  firstNode.addNode(secondNode)
  secondNode.addNode(firstNode)


paths = []
startNode.setVisit(2)
endNode.setVisit(2)
nodeStack = [startNode]
nodeVisits = [[]]
while len(nodeStack) > 0:
  currentNodeStack: "list[Node]" = nodeVisits[-1]
  currentNode = nodeStack[-1]
  impass = True
  spaces = ' ' * (len(nodeStack) - 1)
  foundTwiceVisits = False
  for node in nodeStack:
    if node.isSmall and node.VisitCounter == 2 and node != startNode and node != endNode:
      foundTwiceVisits = True
      break
  for neighbour in currentNode.Nodes:
    if neighbour == endNode and endNode not in currentNodeStack:
      # print(spaces+currentNode.__str__(), neighbour, "END")
      currentNodeStack.append(endNode)
      impass = False
      paths.append(nodeStack.copy())
    elif neighbour not in currentNodeStack and (neighbour.isSmall == False or neighbour not in nodeStack or (foundTwiceVisits == False and neighbour != startNode)):
        # print(spaces+currentNode.__str__(), neighbour, "NEXT")
        currentNodeStack.append(neighbour)
        nodeStack.append(neighbour)
        nodeVisits.append([])
        neighbour.visit()
        impass = False
        break;

  if impass:
    # print(spaces+currentNode.__str__(), "IMPASS")
    nodeStack.pop()
    nodeVisits.pop()
    currentNode.unVisit()
    
# paths.sort(key=len)
for path in paths:
  print(path)
print(len(paths))