import os, sys, re, time
inputText = open(os.path.join(sys.path[0], 'testinput'), 'r')
lines = inputText.readlines()

class CompressedArray:
  def __init__(self):
    self.array = []
    self.counters = []

  def append(self, item):
    if len(self.array) == 0 or self.array[-1] != item:
      self.array.append(item)
      self.counters.append(1)
    else:
      self.counters[-1] += 1

  def appendMultiple(self, item, counter):
    if len(self.array) == 0 or self.array[-1] != item:
      self.array.append(item)
      self.counters.append(counter)
    else:
      self.counters[-1] += counter

  def findInstruction(instructions: "list", left: int, right: int):
    for ins in instructions:
      if ins[0] == left and ins[1] == right:
        return ins
    return None

  def insertInstructions(self, instructions):
    resultArray: "CompressedArray" = CompressedArray()
    leftCounter = 0
    leftSubCounter = 1
    rightCounter = 0
    rightSubCounter = 2
    resultArray.append(self.array[0])
    while True:
      if self.counters[leftCounter] < leftSubCounter:
        leftCounter += 1
        leftSubCounter = 1
        if self.counters[leftCounter] == 1:
          rightCounter = leftCounter+1
          rightSubCounter = 1
        else:
          rightCounter = leftCounter
          rightSubCounter = 2
      elif self.counters[leftCounter] < leftSubCounter + 1:
        rightCounter = leftCounter+1 
        rightSubCounter = 1
      if rightCounter >= len(self.array) or (rightCounter == len(self.array)-1 and rightSubCounter > self.counters[-1]):
        break;
      left = self.array[leftCounter]
      right = self.array[rightCounter]
      instruction = CompressedArray.findInstruction(instructions, left, right)
      if instruction is not None:
        resultArray.append(instruction[2])
      resultArray.append(right)
      leftSubCounter+=1
      rightSubCounter+=1
    self.array = resultArray.array
    self.counters = resultArray.counters

  def copy(self):
    copyArray = CompressedArray()
    copyArray.array = self.array.copy()
    copyArray.counters = self.counters.copy()
    return copyArray
  
  def __str__(self) -> str:
    returnStr = "[ ";
    for i in range(len(self.array)):
      for j in range(self.counters[i]):
        returnStr += self.array[i]
    return returnStr + " ]"
  def __len__(self):
    counter = 0
    for c in self.counters:
      counter += c
    return counter
  def getQuantities(self):
    counters = {}
    for i in range(len(self.array)):
      if self.array[i] in counters:
        counters[self.array[i]] += self.counters[i]
      else:
        counters[self.array[i]] = self.counters[i]
    return counters

polymer = CompressedArray()


for i in range(len(lines[0].strip())):
  char = lines[0].strip()[i]
  polymer.append(char)
print(polymer)
instructions = []
for i in range(2, len(lines)):
  instruction = lines[i].strip().split(' -> ')
  instructions.append([instruction[0][0], instruction[0][1], instruction[1][0]])

lastDiff = 0
for i in range(40):
  starttime = time.time_ns()
  polymer.insertInstructions(instructions)
  endtime = time.time_ns()
  diff = endtime - starttime;
  print(i.__str__()+": ", diff / 1000, "ms")
  print(i.__str__()+": ", (diff - lastDiff)/1000, "ms increase")
  lastDiff = diff
  # print(polymer)
  # print(len(polymer))
  # print(polymer.getQuantities())
min = sys.maxsize
max = 0
quantities = polymer.getQuantities();
for counter in quantities:
  if quantities[counter] < min:
    min = quantities[counter]
  if quantities[counter] > max:
    max = quantities[counter]
print(min, max, max - min)



