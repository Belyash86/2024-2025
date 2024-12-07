k = []
for x in range(1, 1950+1):
    res = 72070 + 7400 - x
    k0 = 0
    while res:
        k0 += res%9 == 0
        res //= 9
    k.append(k0)
print(max(k))