from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1, b), (a*4, b), (a, b+1), (a, b*4)

@lru_cache(None)
def game(h):
    if sum(h) >= 82: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'П1'
    if any(game(x) == 'П1' for x in moves(h)): return 'В1'
    if any(game(x) == 'В1' for x in moves(h)): return 'П2'
    if all(game(x) in ['П1','П2'] for x in moves(h)): return 'В2'

for s in range(1, 77+1):
    g = game((4, s))
    if g != None:
        print(s, g)