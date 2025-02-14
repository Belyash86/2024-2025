def f(n):
    r = bin(n)[2:]
    r = r[1:]
    if r.count('1') % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '0'
    return int(r,2)
print(max(f(n) for n in range(2, 10000) if f(n) < 450))