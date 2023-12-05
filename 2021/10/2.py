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

scores = []

for line in lines:
  currentChunks = []
  incomplete = False
  for char in line.strip():
    if char in "([{<":
      currentChunks.append(getClosingChunk(char))
    else:
      if currentChunks[len(currentChunks) - 1] != char:
        incomplete = True
        break
      currentChunks.pop()
  if not incomplete and len(currentChunks) > 0:
    currentScore = 0
    for i in range(len(currentChunks)-1, -1, -1):
      currentScore *= 5
      if currentChunks[i] == ")":
        currentScore += 1
      elif currentChunks[i] == "]":
        currentScore += 2
      elif currentChunks[i] == "}":
        currentScore += 3
      else:
        currentScore += 4
    scores.append(currentScore)

scores.sort()
print(scores)
print(len(scores)//2)
print(scores[len(scores)//2])