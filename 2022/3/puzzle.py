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

def find_common(comp1: str, comp2: str):
  for index in range(len(comp1)):
    if comp2.__contains__(comp1[index]):
      return comp1[index]
  return ""

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  sum = 0
  for line in lines:
    comp1 = line.strip()[:len(line)//2]
    comp2 = line.strip()[len(line)//2:]
    common = find_common(comp1, comp2)
    prio = to_priority(common)
    print(f"Item: {common}\nPrio: {prio}\n")
    sum += prio
  print(sum)

if __name__ == "__main__":
  main()