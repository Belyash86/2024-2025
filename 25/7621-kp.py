def divs(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return i + n//i
    return 0

k = 0
n = 800001
while k < 5:
    if divs(n)%10 == 4:
        print(n, divs(n))
        k += 1
    n += 1