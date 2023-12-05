"""provides path joining functions annd module joining"""
import os
import sys
import time
from typing import Callable

INPUT_FILE="sample"

class monkey:
  items: list[int]
  op_input: tuple[bool, bool, int]
  test: int
  outcomeTrue: int
  outcomeFalse: int
  max_module: int
  def __init__(self, index: int) -> None:
    self.index = index
    self.inspections = 0
  def operation(self, item) -> int:
    # if it is multiply
    if self.op_input[0]:
      # if both are "old"
      if self.op_input[1]:
        return item*item
      else:
        return item*self.op_input[2]
    return item+self.op_input[2]
  def operation_2(self, item) -> int:
    if self.op_input[0]:
      if self.op_input[1]:
        return (item*item)%self.max_module
      else:
        return (item*self.op_input[2])%self.max_module
    return (item+self.op_input[2])%self.max_module
  def inspectItems(self) -> list[tuple[int, int]]:
    returnList = []
    for item in self.items:
      self.inspections += 1
      item = self.operation(item)
      #item = item // 3
      if item % self.test == 0:
        returnList.append([self.outcomeTrue, item])
      else:
        returnList.append([self.outcomeFalse, item])
    return returnList
  def __repr__(self) -> str:
    return f"Monkey {self.index}: "+", ".join(map(str, self.items))
    

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  monkeys: list[monkey] = []
  currentMonkey = None
  currentLineCounter = 0
  max_modulo = 1
  for line in lines:
    # if new monkey definition started (Monkey 0:)
    if currentMonkey == None:
      currentMonkey = monkey(len(monkeys))
      monkeys.append(currentMonkey)
      currentLineCounter = 1
      continue
    # if new line appeared:
    if line.strip() == "":
      currentMonkey = None
      continue
    match currentLineCounter:
      case 1:
        currentMonkey.items = list(map(int, line.strip().split(": ")[1].split(", ")))
      case 2:
        operation = line.strip().split("= ")[1]
        real_split = operation.split(" * ")
        is_mult = len(real_split) > 1
        if not is_mult:
          real_split = operation.split(" + ")
        both_old = real_split[0] == "old" and real_split[1] == "old"
        num = 0
        if not both_old and real_split[0] != "old":
          num = int(real_split[0])
        elif not both_old and real_split[1] != "old":
          num = int(real_split[1])
        currentMonkey.op_input = (is_mult, both_old, num)
      case 3:
        currentMonkey.test = int(line.strip().split(" by ")[1])
        max_modulo *= currentMonkey.test
      case 4:
        currentMonkey.outcomeTrue = int(line.strip().split(" monkey ")[1])
      case 5:
        currentMonkey.outcomeFalse = int(line.strip().split(" monkey ")[1])
    currentLineCounter += 1
  for current in monkeys:
    current.max_module = max_modulo
  # starting rounds
  # for i in range(20)
  for i in range(4):
    for current in monkeys:
      items = current.inspectItems()
      newMonkeyItems: list[int] = []
      for item in items:
        if current.index == item[0]:
          newMonkeyItems.append(item[1])
          continue
        monkeys[item[0]].items.append(item[1])
      current.items = newMonkeyItems
    for current in monkeys:
     print(current.__repr__())
  inspections = []
  for current in monkeys:
    print(f"Monkey {current.index} inspected items {current.inspections} times.")
    inspections.append(current.inspections)
  inspections.sort(reverse=True)
  print(f"Result: {inspections[0]*inspections[1]}")
    
if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")