from math import prod
k = 0
for s in open('1.txt'):
    l = sorted([int(x) for x in s.split()])
    u1 = l[-1]**2 > prod(l[:-1])
    u2 = sum(l[-2:])*2 > sum(l[:-2])
    if u1 and u2: k += 1
print(k)