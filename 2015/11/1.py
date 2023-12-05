import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()

def test_password(password: str):
    if "i" in password or "o" in password or "l" in password:
        return False
    found_continuous = False
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 == ord(password[i+2])-2:
            found_continuous = True
            break
    if not found_continuous:
        return False
    found_two_pairs = False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            for j in range(i+2, len(password)-1):
                if password[j] == password[j+1]:
                    found_two_pairs = True
                    break
            if found_two_pairs:
                break
    return found_two_pairs

def next_password(password: str):
    password = list(password)
    for i in range(len(password)-1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
        else:
            password[i] = chr(ord(password[i])+1)
            break
    return "".join(password)
password = next_password(text)
while not test_password(password):
    password = next_password(password)
print(password)
    
