"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"

def transform(pair:str):
  split = pair.split("-")
  return (int(split[0], 10), int(split[1], 10))

def total_overlap(pair1: tuple[int, int], pair2: tuple[int, int]):
  if pair1[0] == pair2[0] or pair1[1] == pair2[1]:
    return True
  if pair1[0] < pair2[0]:
    if pair1[1] > pair2[1]:
      return True
  elif pair2[0] < pair1[0]:
    if pair2[1] > pair1[1]:
      return True
  return False


def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  
  counter = 0
  for line in lines:
    pair1 = line.strip().split(",")[0]
    pair2 = line.strip().split(",")[1]
    if total_overlap(transform(pair1), transform(pair2)):
      counter+=1
  print(counter)

if __name__ == "__main__":
  main()