import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

unique = [2, 4, 3, 7]

counter = 0
for line in lines:
  match = re.search(".+\| (.+) (.+) (.+) (.+)", line.strip())
  # print(match.groups())
  word1, word2, word3, word4 = len(match.group(1)), len(match.group(2)), len(match.group(3)), len(match.group(4))
  # print(word1, word2, word3, word4)
  # prevCounter = counter
  if word1 in unique:
    counter += 1
  if word2 in unique:
    counter += 1
  if word3 in unique: 
    counter += 1
  if word4 in unique:
    counter +=1
  # print(counter - prevCounter)
print(counter)