import os, sys
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

fishes = [0,0,0,0,0,0,0,0,0]
for i in range(0, len(lines[0]), 2):
    fishes[int(lines[0][i])] += 1;
print(fishes)
for i in range(256):
    zeroDayFishes = fishes.pop(0);
    fishes[6]+=zeroDayFishes;
    fishes.append(zeroDayFishes);
    # print(fishes)
sum = 0
for fish in fishes:
    sum += fish;
print(sum)