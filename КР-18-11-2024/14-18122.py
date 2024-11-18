for x in range(5555, 1, -1):
    res = 5**150 + 5**135 - x
    k4 = 0
    while res:
        k4 += res%5 == 4
        res //= 5
    if k4 == 134:
        print(x)
        break