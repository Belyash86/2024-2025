def d(x, y):
    return x%y == 0

for A in range(1, 500):
    k = 0
    for x in range(1, 1000+1):
        k += ((not d(x, 7) and d(x, 13)) <= (x > A - 40))
    if k == 1000:
        print(A)