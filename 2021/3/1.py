import os, sys
input = open(os.path.join(sys.path[0], 'input'), 'r')
lines = input.readlines()

gammaString = ""
epsilonString = ""
for i in range(12):
  count = 0;
  for line in lines:
    if line[i] == '1':
      count += 1
  if count > len(lines)/2:
    gammaString += "1"
    epsilonString += "0"
  else:
    gammaString += "0"
    epsilonString += "1"

gamma = int(gammaString, 2)
epsilon = int(epsilonString, 2)

print("gamma ", gammaString, gamma)
print("epsilon ", epsilonString, epsilon)
print("Product ", gamma * epsilon)