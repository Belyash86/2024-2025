for x in range(2030, 1, -1):
    y = 6**260 + 6**160 + 6**60 - x
    k0 = 0
    while y:
        if y%6 == 0:
            k0 += 1
        y //= 6
    if k0 == 202:
        print(x)
        exit()