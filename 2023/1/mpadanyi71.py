word_to_num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
num_list = []
char_list = []
sum = 0
y = 0
first_letter = ["o", "t", "f", "s", "e","n"]
second_letter = ["n","w","h","o","i","e","i"]
third_letter = ["e","o","r","u","v","x","g","n"]
fourth_letter = ["e","r","h"]
fith_letter = ["t","e","n"]

with open("./1/example2", "r") as f:
    txt = f.read()

for item in txt:

    if item.isdigit():
        num_list.append(item)
        y = 0
    elif item == "\n":
        num = num_list[0] + num_list[-1]
        num = int(num)
        print(num)
        sum += num
        num_list.clear()
        word = ""
        char_list.clear()
        y = 0
    else:
        if item in first_letter and y == 0:
            char_list.append(item)
            y += 1
        elif item in second_letter and y == 1:
            char_list.append(item)
            word = "".join(char_list)
            if word == "on" or word == "tw" or word == "th" or word == "fo" or word == "fi" or word == "si" or word == "se" or word == "ei" or word == "ni":
                y += 1
            else:
                y = 0
                word = ""
                char_list.clear()
        elif item in first_letter and y == 1:
            char_list.clear()
            char_list.append(item)
        elif item in third_letter and y == 2:
            char_list.append(item)
            word = "".join(char_list)
            if word == "one" or word == "two" or word == "six":
                word = word_to_num.get(word)
                num_list.append(word)
                word = ""
                char_list.clear()
                y = 0
            elif word == "thr" or word == "fou" or word == "fiv" or word == "sev" or word == "eig" or word == "nin":
                y += 1
            else:
                y = 0
                word = ""
                char_list.clear()
        elif item in fourth_letter and y == 3:
            char_list.append(item)
            word = "".join(char_list)
            if word == "five" or word == "four" or word == "nine":
                word = word_to_num.get(word)
                num_list.append(word)
                y = 0
                word = ""
                char_list.clear()
            elif word == "thre" or word == "seve" or word == "eigh":
                y += 1
            else:
                y = 0
                word = ""
                char_list.clear()
        elif item in fith_letter and y == 4:
            char_list.append(item)
            word = "".join(char_list)
            if word == "three" or word == "seven" or word == "eight":
                word = word_to_num.get(word)
                num_list.append(word)
                word = ""
                char_list.clear()
                y = 0
            elif item in first_letter:
                char_list.clear()
                y = 0
                char_list.append((item))
            else:
                y = 0
                word = ""
                char_list.clear()
        else:
            y = 0
            word = ""
            char_list.clear()

num = num_list[0] + num_list[-1]
num = int(num)
print(num)
sum += num
print(sum)