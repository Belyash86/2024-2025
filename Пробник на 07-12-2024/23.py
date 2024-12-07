def f(c, e):
    if c>e or c == 35: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+2, e) + f(c+4, e)

print(f(24,33) * f(33,42))