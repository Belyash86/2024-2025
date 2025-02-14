from functools import lru_cache

def moves(h):
    a,b = h
    if a == b:
        return (a+1,b), (a+2,b), (a+3,b), (a,b+1), (a,b+2), (a,b+3)
    else:
        return (min(a,b), max(a,b)+1), (min(a,b), max(a,b)+2), (min(a,b), max(a,b)+3), (min(a,b)*2, max(a,b))

@lru_cache(None)
def game(h):
    if sum(h) >= 60: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'P1'
    if all(game(x) == 'P1' for x in moves(h)): return 'V1'
    if any(game(x) == 'V1' for x in moves(h)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(h)): return 'V2'

for s in range(1,47+1):
    g = game((12,s))
    if g == 'P2':
        print(s, g)