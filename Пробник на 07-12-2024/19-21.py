from math import ceil
from functools import lru_cache
def moves(h):
    return h-2, h-4, ceil(h/2)

@lru_cache(None)
def game(h):
    if h <= 35: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'П1'
    if all(game(x) == 'П1' for x in moves(h)): return 'В1'
    if any(game(x) == 'В1' for x in moves(h)): return 'П2'
    if all(game(x) in ['П1','П2']  for x in moves(h)): return 'В2'

for s in range(36, 1000+1):
    g = game(s)
    if g == 'В2':
        print(s, g)