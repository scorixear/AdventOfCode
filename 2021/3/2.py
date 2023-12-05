import os, sys
input = open(os.path.join(sys.path[0], 'input'), 'r')
lines = input.readlines()

oxygenNumbers = lines.copy()
co2Numbers = lines.copy()
oxygenNumber = ""
co2Number = ""

oxygenRating = 0
co2Rating = 0

for i in range(len(lines[0])):
  oxygenLines1 = []
  oxygenLines0 = []
  
  for line in oxygenNumbers:
    if line[i] == '1':
      oxygenLines1.append(line)
    else:
      oxygenLines0.append(line)
  
  if len(oxygenLines1) >= len(oxygenLines0):
    oxygenNumbers = oxygenLines1.copy()
  else:
    oxygenNumbers = oxygenLines0.copy()
  if len(oxygenNumbers) == 1:
    oxygenRating = int(oxygenNumbers[0],2)
    break

for i in range (len(lines[0])):
  co2Lines1 = []
  co2Lines0 = []
  for line in co2Numbers:
    if line[i] == '1':
      co2Lines1.append(line)
    else:
      co2Lines0.append(line)
  if len(co2Lines1) < len(co2Lines0):
    co2Numbers = co2Lines1.copy()
  else:
    co2Numbers = co2Lines0.copy()
  if len(co2Numbers) == 1:
    co2Rating = int(co2Numbers[0],2)
    break

print("O2 Rating", oxygenNumbers[0], oxygenRating)
print("CO2 Rating", co2Numbers[0], co2Rating)
print("Product ", oxygenRating * co2Rating)
  