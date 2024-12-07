def f(n):
    r = bin(n)[2:]
    r += str(r.count('1')%2)
    r += str(r.count('1')%2)
    return int(r, 2)
print(min([f(n) for n in range(1, 10000) if f(n)>198]))