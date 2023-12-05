import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

# remove every char of decoded from segments, if present and return length of lefover segments
def getRemovedSegments(segments: "str", decoded: "str"):
  testSegments = list(segments)
  for segment in decoded:
    if segment in testSegments: testSegments.remove(segment)
  return len(testSegments)

# Unique Lenght Mapping to corresponding Value
unique = { 2: 1, 4: 4, 3: 7, 7: 8}
# total Sum for output
sum = 0

# for each given display
for line in lines:
  # decoded will contain all numbers and their corresponding segments
  decoded = {}
  # split line into unique patterns and resulting number
  parts = line.strip().split(' | ')
  part1Numbers = parts[0].split(' ')
  part2Numbers = parts[1].split(' ')

  # first we add all unique length numbers to decoded
  # for each number in segments
  for part in part1Numbers:
    if len(part) in unique.keys():
      decoded[unique[len(part)]] = part
  # then we deduct from the given unique sequences, which number it must be
  for part in part1Numbers:
    # if number is not already in decoded
    if len(part) not in unique.keys():
      # if you remove all Segments from the number '1' of the number '3', only 3 segments stay lit up.
      # only number 3 has this property
      if getRemovedSegments(part, decoded[1]) == 3:
        decoded[3] = part
      # same goes for number 7 and 6 resulting in 4 lit up segments
      elif getRemovedSegments(part, decoded[7]) == 4:
        decoded[6] = part
      # otherwise, we have either 0 or 9 with 6 segments, or 2 and 5 wth 5 segments
      elif len(part) == 6:
        # removing the segments from 4 of 0 returns 3 segments, in the case of 9 it would return 2 segments
        if getRemovedSegments(part, decoded[4]) == 3:
          decoded[0] = part
        else:
          decoded[9] = part
      else:
        # removing the segments from 4 of 2 return 3 segments, in the case of 5 it would return 2 segments
        if getRemovedSegments(part, decoded[4]) == 3:
          decoded[2] = part
        else:
          decoded[5] = part
  
  # total number for this display
  totalNumber = 0
  # power of ten to calculate total number
  power = 3
  # for each digit of the number
  for part2 in part2Numbers:

    foundValue = -1
    # for all decoded Values
    for decodedKey in decoded:
      # if the digit segments are equal to the decoded segments (sorted)
      # we found the value
      if "".join(sorted(decoded[decodedKey])) == "".join(sorted(part2)): 
        foundValue = decodedKey
        break
    # add the digit in the correct position
    totalNumber += foundValue * pow(10, power)
    power -= 1
  sum += totalNumber
print(sum)
