def f(c, e):
    if c == e: return 1
    if c < e: return 0
    return f(c-4, e) + f(c-7, e) + f(int(c**0.5), e)

print(f(44, 22) * f(22, 3))