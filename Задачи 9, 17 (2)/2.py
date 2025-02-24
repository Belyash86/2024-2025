k = 0
for s in open('2.txt'):
    l = sorted([int(x) for x in s.split()])
    p = [x for x in l if l.count(x) > 1]
    np = [x for x in l if l.count(x) == 1]
    u1 = len(p) == 0 and int((l[0]+l[-1])/2) in l
    u2 = len(p) > 0 and sum([x**2 for x in p]) < sum([x**2 for x in np])
    if (u1 and u2 == False) or (u1 == False and u2):
        k += 1
print(k)
