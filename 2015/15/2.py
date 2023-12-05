import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    parsed_ingredients = []
    for line in lines:
        line = line.replace(",", "").split(" ")
        parsed_ingredients.append([int(line[2]), int(line[4]), int(line[6]), int(line[8]), int(line[10])])
max_score = 0
def get_max_score(ingredients: list, cap, dur, fla, tex, cal, left_over):
    ingredient = ingredients[0]
    
    if len(ingredients) == 1:
        global max_score
        cap += left_over*ingredient[0]
        dur += left_over*ingredient[1]
        fla += left_over*ingredient[2]
        tex += left_over*ingredient[3]
        cal += left_over*ingredient[4]
        if cap < 0 or dur < 0 or fla < 0 or tex < 0 or cal != 500:
            return
        max_score = max(max_score, cap*dur*fla*tex)
    else:
        for i in range(left_over+1):
            new_cap = cap + i*ingredient[0]
            new_dur = dur + i*ingredient[1]
            new_fla = fla + i*ingredient[2]
            new_tex = tex + i*ingredient[3]
            new_cal = cal + i*ingredient[4]
            get_max_score(ingredients[1:], new_cap, new_dur, new_fla, new_tex, new_cal, left_over-i)
get_max_score(parsed_ingredients, 0, 0, 0, 0, 0, 100)
print(max_score)
            