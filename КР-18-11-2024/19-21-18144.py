from functools import lru_cache
from math import ceil
def moves(h):
    return h-4, h-6, ceil(h/2)

@lru_cache(None)
def game(h):
    if h <= 19: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'П1'
    if all(game(x) == 'П1' for x in moves(h)): return 'В1'
    if any(game(x) == 'В1' for x in moves(h)): return 'П2'
    if all(game(x) in ['П1','П2']  for x in moves(h)): return 'В2'

for s in range(20, 1000+1):
    g = game(s)
    if g != None:
        print(s, g)