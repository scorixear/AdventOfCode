"""provides path joining functions annd module joining"""
import os
import sys
import time

INPUT_FILE="input"

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  current_index = 0
  x_register = 1
  cycle_counter = 1
  is_addx = False
  
  display: list[str] = ["" for i in range(6)]
  
  while True:
    
    # draw pixel
    pixelPos = (cycle_counter-1)%40
    rowPos = (cycle_counter-1)//40
    if x_register-1 <= pixelPos and x_register+1 >= pixelPos:
      display[rowPos] = display[rowPos] + "██"
    else:
      display[rowPos] = display[rowPos] + "  "
    
    
    
    ###### assembly handling ######
    # read in line
    line = lines[current_index].strip()
    # if line is addx
    if line != "noop":
      # if this is second cycle of addx
      if is_addx:
        # add value to x_register
        x_register += int(line.split(" ")[1])
        # return to default
        is_addx = False
        # increase line
        current_index+=1
      # if this is first cycle of addx
      else:
        # do nothing, mark as done
        is_addx = True
    # if this is noop
    else:
      # do nothing, next line
      current_index+=1
    # increase cycle counter
    cycle_counter+=1
    # if all lines are read, program stops
    if current_index >= len(lines) or cycle_counter > 240:
      break
  for line in display:
    print(line)


# puzzle handling
if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms");