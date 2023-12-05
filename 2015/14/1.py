import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    max_travel = 0
    travel_time = 2503
    for line in lines:
        line = line.split(" ")
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[-2])
        
        time_mod = travel_time // (fly_time + rest_time) 
        left_over = travel_time % (fly_time + rest_time)
        distance = speed * fly_time * time_mod
        if left_over >= fly_time:
            distance += speed * fly_time
        else:
            distance += speed * left_over
        max_travel = max(max_travel, distance)
    print(max_travel)
        
    
