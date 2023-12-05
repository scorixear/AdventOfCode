import math
import os, sys


class Node:
    def __init__(self, name):
        self.name = name
        self.next = []
    def addNext(self, node):
        self.next.append(node)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    state_lines = {}
    states = set()
    for line in lines:
        line = line.split(" ")
        state_lines[(line[0], line[2])] = int(line[4])
        state_lines[(line[2], line[0])] = int(line[4])
        states.add(line[0])
        states.add(line[2])
def bfs(current, left_over):
    if len(left_over) == 0:
        return 0
    result = math.inf
    for i, state in enumerate(left_over):
        new_left_over = left_over[:i] + left_over[i+1:]
        result = min(result, bfs(state, new_left_over) + state_lines[(current, state)])
    return result

minimum_state = math.inf
states = list(states)
for i, state in enumerate(states):
    left_over = states[:i] + states[i+1:]
    minimum_state = min(minimum_state, bfs(state, left_over))
print(minimum_state)
    
