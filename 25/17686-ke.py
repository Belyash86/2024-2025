def divs(n):
    for i in range(17, n, 10):
        if n%i == 0:
            return i
    return False

k = 0
n = 700001
while k < 5:
    if divs(n):
        print(n, divs(n))
        k += 1
    n += 1