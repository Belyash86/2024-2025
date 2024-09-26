def f(c, e):
    if c == e: return 1
    if c < e or c == 12: return 0
    return f(c-3, e) + f(c//2, e)

print(f(80, 23)*f(23, 3))