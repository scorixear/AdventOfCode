number = 33100000
houses = [0] * (number//10 + 1)
for i in range(1, number//10 + 1):
    for j in range(i, number//10 + 1, i):
        houses[j] += i*10
for i in range(1, number//10 + 1):
    if houses[i] >= number:
        print(i)
        break
