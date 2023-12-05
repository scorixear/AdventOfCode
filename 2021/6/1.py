import os, sys
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

fishes = []
for i in range(0, len(lines[0]), 2):
    fishes.append(int(lines[0][i]));
print(fishes)
for i in range(80):
    newFishes = []
    for index in range(len(fishes)):
        fishes[index] -= 1
        if fishes[index] == -1:
            fishes[index] = 6
            newFishes.append(8)
    fishes.extend(newFishes)
print(len(fishes))
