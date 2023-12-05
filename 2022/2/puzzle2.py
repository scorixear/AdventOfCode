"""provides path joining functions annd module joining"""
import os
import sys

INPUT_FILE="input"


def obj_to_score(player, opponent):
  match player:
    case "X":
      match opponent:
        case "A":
          return 3
        case "B":
          return 1
        case _:
          return 2
    case "Y":
      match opponent:
        case "A":
          return 1
        case "B":
          return 2
        case _:
          return 3
    case _:
      match opponent:
        case "A":
          return 2
        case "B":
          return 3
        case _:
          return 1
def game_score(player):
  match player:
    case "X":
      return 0
    case "Y":
      return 3
    case _:
      return 6


def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  
  total_score = 0
  for line in lines:
    opponent = line.strip().split(' ')[0]
    player = line.strip().split(' ')[1]
    total_score += obj_to_score(player, opponent) + game_score(player)
  print(total_score)

if __name__ == "__main__":
  main()