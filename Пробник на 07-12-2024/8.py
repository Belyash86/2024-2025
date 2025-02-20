from itertools import permutations
k = 0
for p in set(permutations('АРТЁМ')):
    s = ''.join(p)
    if not(s[0] in 'АЁ' and s[-1] in 'АЁ'):
        k += 1
print(k)