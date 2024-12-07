def d(n, m):
    return n%m == 0

def f(x, A):
    return (not(d(x, A)) and (132<=x<=150)) <= (not(d(x, 13)))

for A in range(2, 100):
    if all(f(x, A) for x in range(1, 10000)):
        print(A)
        exit()

