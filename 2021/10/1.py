import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

def getClosingChunk(chunk):
  if chunk == "(":
    return ")"
  elif chunk == "[":
    return "]"
  elif chunk == "{":
    return "}"
  else:
    return ">"

sum = 0

for line in lines:
  currentChunks = []
  for char in line.strip():
    if char in "([{<":
      currentChunks.append(getClosingChunk(char))
    else:
      if currentChunks[len(currentChunks) - 1] != char:
        print(line.strip(), f"- Expected {currentChunks[len(currentChunks)-1]}, but found {char} instead")
        if char == ")":
          sum += 3
        elif char == "]":
          sum += 57
        elif char == "}":
          sum += 1197
        else:
          sum += 25137
        break
      currentChunks.pop()

print(sum)