k = 0
for s in open('1.txt'):
    l = [int(x) for x in s.split()]
    p3 = [x for x in l if l.count(x) == 3]
    np = [x for x in l if l.count(x) == 1]
    if len(p3)>0 and len(np)>0:
        u1 = len(set(p3)) == 2 and len(np) == 1
        u2 = (sum(p3)/len(p3)) < np[0]
        if u1 and u2:
            k += np[0]
print(k)
