from itertools import permutations
k = 0
for p in set(permutations('ТРЕНБОЛОН')):
    s = ''.join(p)
    l, r = s.find('О'), s.rfind('О')
    if 'Б' in s[l+1: r]:
        k += 1
print(k)