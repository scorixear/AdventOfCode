import os, sys
from itertools import permutations

def readInput() -> dict[str, dict[str, int]]:
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
        participants = {}
    start = None
    for line in lines:
        line = line.replace(".", "").split(" ")
        person = line[0]
        if start is None:
            start = person
        gain = int(line[3])
        if line[2] == "lose":
            gain *= -1
        neighbour = line[-1]
        if person not in participants:
            participants[person] = {}
        participants[person][neighbour] = gain
    return participants
    
    
def getHappiness(participants: dict[str, dict[str, int]] , order: list[str]) -> int:
    happiness = 0
    for i, person in enumerate(order):
        left = order[i-1]
        right = order[(i+1)%len(order)]
        happiness += participants[person][left] + participants[person][right]
    return happiness

def getBestHappiness(participants: dict[str, dict[str, int]]):
    best_happiness = 0
    best_order = []
    perms = permutations(participants.keys())
    for order in perms:
        happiness = getHappiness(participants, order)
        if happiness > best_happiness:
            best_happiness = happiness
            best_order = order
    return best_happiness, best_order

party = readInput()
party["Me"] = {}
for person in party.keys():
    party[person]["Me"] = 0
    party["Me"][person] = 0
answer, answer_oder = getBestHappiness(party)
print(answer, answer_oder)
