"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"

def notation_to_obj(notation):
 if notation == "A" or notation == "X":
   return "R"
 elif notation == "B" or notation == "Y":
   return "P"
 else:
   return "S"

def obj_to_score(notation):
  obj = notation_to_obj(notation)
  match obj:
    case "R":
      return 1
    case "P":
      return 2
    case "S":
      return 3
  return 0
def game_score(playernot, opponentnot):
  player = notation_to_obj(playernot)
  opponent = notation_to_obj(opponentnot)
  if player == opponent:
    return 3
  if player == "R":
    if opponent == "P":
      return 0
  elif player == "P":
    if opponent == "S":
      return 0
  else:
    if opponent == "R":
      return 0
  return 6


def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  
  total_score = 0
  for line in lines:
    opponent = line.strip().split(' ')[0]
    player = line.strip().split(' ')[1]
    total_score += obj_to_score(player) + game_score(player, opponent)
  print(total_score)

if __name__ == "__main__":
  main()