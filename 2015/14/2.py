import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    reindeers = []
    travel_time = 2503
    for line in lines:
        line = line.split(" ")
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[-2])
        reindeers.append([speed, fly_time, rest_time])
        
    points = [0] * len(reindeers)
    position = [0] * len(reindeers)
    for i in range(travel_time):
        for j in range(len(reindeers)):
            if i % (reindeers[j][1] + reindeers[j][2]) < reindeers[j][1]:
                position[j] += reindeers[j][0]
        max_position = max(position)
        for j in range(len(reindeers)):
            if position[j] == max_position:
                points[j] += 1
    print(max(points))
        
    
