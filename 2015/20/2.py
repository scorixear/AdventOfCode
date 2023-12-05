number = 33100000
houses = [0] * (number//11 + 1)
for i in range(1, number//11 + 1):
    for j in range(i, number//11 + 1, i):
        if j <= i*50:
            houses[j] += i*11
for i in range(1, number//11 + 1):
    if houses[i] >= number:
        print(i)
        break
