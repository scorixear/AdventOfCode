"""provides path joining functions annd module joining"""
import os
import sys
import time
import re
from functools import reduce

INPUT_FILE="input"
SELECTED_Y = 2_000_000

def get_overlap(sensor, beacon):
  max_reach = (abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1]))
  x_reach = 0
  if SELECTED_Y > sensor[1]:
    if SELECTED_Y - sensor[1] > max_reach:
      return None
    else:
      x_reach = (max_reach - (SELECTED_Y - sensor[1]))
  else:
    if sensor[1] - SELECTED_Y > max_reach:
      return None
    else:
      x_reach = (max_reach - (sensor[1] - SELECTED_Y))
  return (sensor[0] - x_reach, sensor[0] + x_reach)
def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  positions: list[tuple[tuple[int, int], tuple[int, int]]] = []
  for line in lines:
    pos = re.match("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)", line.strip())
    if pos is None:
      raise ValueError
    sensor = (int(pos.groups()[0]), int(pos.groups()[1]))
    beacon = (int(pos.groups()[2]), int(pos.groups()[3]))
    positions.append((sensor, beacon))
    
  fitting_beacons = [p[1][0] for p in filter(lambda p: p[1][1] == SELECTED_Y, positions)]
  spans: list[tuple[int, int]] = []
  for position in positions:
    overlap = get_overlap(position[0], position[1])
    if overlap is not None:
      spans.append(overlap)
  spans.sort(key=lambda s: s[0])
  min_x = spans[0][0]
  max_spans = sorted(spans, key=lambda s: s[1])
  max_x = max_spans[-1][1]
  row = [False for _ in range(min_x, max_x+1)]
  for span in spans:
    for i in range(span[0], span[1]+1):
      row[i-min_x] = True
  for beacon in fitting_beacons:
    row[beacon - min_x] = False
  count = reduce(lambda total,element: total + 1 if element else total, row)
  print(count)
  #distinct_spans: list[tuple[int, int]] = []
  #total_covered = 0
  #for span in spans:
  #  to_be_added = span[1] - span[0]
  #  add_to_distinct = True
  #  for other in distinct_spans:
  #    if other[0] <= span[0]:
  #      if other[1] >= span[0]:
  #        overlap = other[1] - span[0] + 1
  #        if to_be_added - overlap <= 0:
  #          add_to_distinct = False
  #          break
  #        else:
  #          to_be_added -= overlap
  #      else:
  #        continue
  #    else:

  
  


if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")