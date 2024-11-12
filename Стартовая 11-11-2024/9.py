k = 0
for f in open('9.txt'):
    l = sorted([int(x) for x in f.split()])
    if (l[0]+l[3]) < sum(l[1:3]): k += 1
print(k)
