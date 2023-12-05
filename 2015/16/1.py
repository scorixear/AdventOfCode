import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
   
    required_combinations = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
   
    for line in lines:
        aunt, categories = line.split(": ", 1)
        aunt_num = int(aunt[4:])
        categories = categories.split(", ")
        isChecked = True
        for category in categories:
            cat, num = category.split(": ")
            num = int(num)
            if num != required_combinations[cat]:
                isChecked = False
                break
        if isChecked:
            print(aunt_num)
            break
            
                
            