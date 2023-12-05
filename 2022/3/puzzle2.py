"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"

def to_priority(item: str):
  if item == "":
    return 0
  asc = ord(item)
  if asc > 96:
    return asc - 96
  else:
    return asc - 64 + 26

def find_common(ruck1: str, ruck2: str, ruck3):
  for index in range(len(ruck1)):
    if ruck1[index] in ruck2 and ruck1[index] in ruck3:
      return ruck1[index]
  return ""

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  sum = 0
  rucksacks = []
  for line in lines:
    if len(rucksacks) < 2:
      rucksacks.append(line.strip())
    else:
      rucksacks.append(line.strip())
      common = find_common(rucksacks[0], rucksacks[1], rucksacks[2])
      prio = to_priority(common)
      print(f"Item: {common}\nPrio: {prio}\n")
      sum += prio
      rucksacks=[]
  print(sum)

if __name__ == "__main__":
  main()