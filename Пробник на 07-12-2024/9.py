k = 0
for s in open('9.txt'):
    l = sorted([int(x) for x in s.split()])
    if len(l) == len(set(l)) and ((l[0]+l[3])/2 <= (l[1]+l[2])/2):
        k += 1
print(k)