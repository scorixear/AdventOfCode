"""provides path joining functions annd module joining"""
import os
import sys
import time
from typing import Optional
from enum import Enum
from functools import cmp_to_key

class Comparison(Enum):
  LEFT = -1
  SAME = 0
  RIGHT = 1

INPUT_FILE="input"
class Item:
  items: list["Item"]
  value: int | None
  parent: Optional["Item"]
  def __init__(self):
    self.items = []
    self.value = None
  def __repr__(self) -> str:
    if self.value is not None:
      return str(self.value)
    return "[" + ",".join(list(map(lambda i:i.__repr__(), self.items))) + "]"
  def parse(self, input: str):
    currentItem: Item | None = self
    currentNumber = ""
    for char in input[1:-1]:
      if currentItem is None:
          raise ValueError()
      if char == "[":
        newItem = Item()
        newItem.parent = currentItem
        currentItem.items.append(newItem)
        currentItem = newItem
      elif char == "]":
        if currentNumber != "" and currentItem is not None:
          newItem = Item()
          newItem.value = int(currentNumber)
          newItem.parent = currentItem
          currentNumber = ""
          currentItem.items.append(newItem)
        currentItem = currentItem.parent
      elif char == ",":
        if currentNumber != "":
          newItem = Item()
          newItem.value = int(currentNumber)
          newItem.parent = currentItem
          currentNumber = ""
          currentItem.items.append(newItem)
      else:
        currentNumber += char
    if currentNumber != "" and currentItem is not None:
      newItem = Item()
      newItem.value = int(currentNumber)
      newItem.parent = currentItem
      currentItem.items.append(newItem)
  def compare(self, other: "Item") -> Comparison:
    if self.value is not None and other.value is not None:
      if self.value < other.value:
        return Comparison.LEFT
      elif self.value == other.value:
        return Comparison.SAME
      else:
        return Comparison.RIGHT
    elif self.value is None and other.value is None:
      for index, left in enumerate(self.items):
        if len(other.items) <= index:
          return Comparison.RIGHT
        right = other.items[index]
        comparison = left.compare(right)
        if comparison != Comparison.SAME:
          return comparison
      if len(self.items) < len(other.items):
        return Comparison.LEFT
      return Comparison.SAME
    elif self.value is not None and other.value is None:
      cover = Item()
      cover.items.append(self)
      return cover.compare(other)
    else:
      cover = Item()
      cover.items.append(other)
      return self.compare(cover)
    
def customCompare(a: Item, b: Item) -> int:
  return a.compare(b).value

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  leftItems: list[Item] = []
  rightItems: list[Item] = []
  count = False
  for line in lines:
    if line.strip() == "":
      count = False
      continue
    currentItem = Item()
    currentItem.parse(line.strip())
    if count == False:
      leftItems.append(currentItem)
      count = True
    else:
      rightItems.append(currentItem)
  # part 1
  total = 0
  for index, leftItem in enumerate(leftItems):
    rightItem = rightItems[index]
    comparison = leftItem.compare(rightItem)
    if  comparison == Comparison.LEFT or comparison == Comparison.SAME:
      total += index+1
  print(total)
  
  # part 2
  items = leftItems + rightItems
  item_2 = Item()
  item_6 = Item()
  item_2.items.append(Item())
  item_2.items[0].items.append(Item())
  item_2.items[0].items[0].value = 2
  item_6.items.append(Item())
  item_6.items[0].items.append(Item())
  item_6.items[0].items[0].value = 6
  items.append(item_2)
  items.append(item_6)
  items.sort(key=cmp_to_key(customCompare))
  total = 1
  for index, item in enumerate(items):
    print(item.__repr__())
    if item == item_2 or item == item_6:
      total *= index+1
  print(total)
      

if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")