import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    count = 0
    for line in lines:
        check_vowel = 0
        check_double = False
        check_banned = True
        if line[0] in ["a", "e", "i", "o", "u"]:
           check_vowel += 1
        for i in range(1, len(line)):
            if line[i] in ["a", "e", "i", "o", "u"]:
                check_vowel += 1
            if line[i] == line[i-1]:
                check_double = True
            if line[i-1] + line[i] in ["ab", "cd", "pq", "xy"]:
                check_banned = False
        if check_vowel >= 3 and check_double and check_banned:
            count += 1
    print(count)
