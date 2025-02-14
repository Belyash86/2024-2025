for x in range(1, 100000):
    p = 3**200 + 3**10 - x
    k2 = 0
    while p:
        k2 += (p%3)==2
        p //= 3
    if k2 == 200:
        print(x)
        break