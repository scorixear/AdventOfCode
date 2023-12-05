import os, sys
input = open(os.path.join(sys.path[0], 'input'), 'r')
lines = input.readlines()

class BingoNumber:
  def __init__(self, number: int):
    self.number = number
    self.hit = False

class Board:
  
  def __init__(self, inputLines: "list[list[BingoNumber]]"):
    self.board: "list[list[BingoNumber]]" = []
    for line in inputLines:
      bingoRow = []
      columns = line.split()
      for column in columns:
        bingoRow.append(BingoNumber(int(column)))
      self.board.append(bingoRow)
  
  def bingoCall(self, number: int):
    for row in self.board:
      isHit = False
      for column in row:
        if column.number == number:
          column.hit = True
          isHit = True
          break
      if isHit:
        break
  def checkBoard(self) -> int:
    # check rows
    for row in self.board:
      isHit = True
      for column in row:
        if column.hit == False:
          isHit = False
          break
      if isHit:
        return self.calculateSum()
    #check columns
    for i in range(5):
      isHit = True
      for row in self.board:
        if row[i].hit == False:
          isHit = False
      if isHit:
        return self.calculateSum()
    return 0
  def calculateSum(self):
    sum = 0
    for row in self.board:
      for column in row:
        if column.hit == False:
          sum += column.number
    return sum


input = lines[0].split(',')
i = 2
boards = []

while i < len(lines):
  boardLines = [lines[i].strip(), lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
  boards.append(Board(boardLines))
  i += 6

sum = 0
lastCall = 0
for call in input:
  boardBingo = False
  i = len(boards)-1
  while i >= 0:
    board = boards[i]
    board.bingoCall(int(call))
    tempSum = board.checkBoard()
    if tempSum > 0:
      if(len(boards) == 1):
        sum = tempSum
        boardBingo = True
        break
      else:
        boards.pop(i)
    i -= 1
  if boardBingo:
    lastCall = call
    break

print('Sum', sum)
print('Last Call', lastCall)
print('Product', sum * int(lastCall))


