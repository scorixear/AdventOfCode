"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()

  max_calories = [0,0,0]
  current_calories = 0
  for line in lines:
    if line.strip() == "":
      if max_calories[0] < current_calories:
        max_calories[0] = current_calories
        max_calories.sort()
      current_calories = 0
    else:
      current_calories += int(line.strip(), 10)
  if max_calories[0] < current_calories:
    max_calories[0] = current_calories
  print(f"{sum(max_calories)}")

if __name__ == "__main__":
  main()
