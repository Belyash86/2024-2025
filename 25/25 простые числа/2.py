from fnmatch import fnmatch
def is_prime(n):
    if n%2 == 0: return False
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

k = 0
n = 600001
while k<6:
    if n%6 == 0 and is_prime(n-1) and is_prime(n+1):
        print(n-1, n+1)
        k+=1
    n += 1