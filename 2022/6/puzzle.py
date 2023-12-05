"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()

  marker = 14

  for index, line in enumerate(lines):
    for i in range(len(line.strip())-marker +1):
      if len(set(line[i:i+marker])) == marker:
        print(f"{index}: {i+marker}")
        break
    
if __name__ == "__main__":
  main()