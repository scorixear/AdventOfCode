"""provides path joining functions annd module joining"""
import os
import sys
import re

INPUT_FILE="input"

def move(crates: list[list[str]], crateFrom: int, crateTo: int, amount: int):
  movedItems = crates[crateFrom][-amount:]
  del crates[crateFrom][-amount:]
  movedItems.reverse()
  crates[crateTo].extend(movedItems)
  
def move9001(crates: list[list[str]], crateFrom: int, crateTo: int, amount: int):
  movedItems = crates[crateFrom][-amount:]
  del crates[crateFrom][-amount:]
  crates[crateTo].extend(movedItems)

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  
  switch = True
  crates: list[list[str]] = []
  
  for line in lines:
    if line.strip() == "":
      switch = False
      continue
    if switch:
      if len(crates) == 0:
        crates = [[] for i in range((len(line)-1)//4+1)]
      if "[" in line:
        for i in range(len(crates)):
          if line[i*4] == "[":
            crates[i].insert(0,line[i*4+1])
      else:
        continue
    else:
      match = re.search("move (\d+) from (\d+) to (\d+)", line.strip())
      if match:
        amount = int(match.groups()[0])
        crateFrom = int(match.groups()[1])-1
        crateTo = int(match.groups()[2])-1
        move9001(crates, crateFrom, crateTo, amount)
  answer = ""
  for crate in crates:
    if len(crate) > 0:
      answer = f"{answer}{crate[-1]}"
  print(answer)
      

if __name__ == "__main__":
  main()