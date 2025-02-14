def f(c,e):
    if c == e: return 1
    if c < e: return 0
    return f(c-3, e) + f(c-2, e) + f(c-1, e)

print(f(36, 28) * f(28, 26) * f(26, 13))