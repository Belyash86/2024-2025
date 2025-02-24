k = 0
for s in open('2.txt'):
    l = sorted([int(x) for x in s.split()])
    if abs((l[3]-l[0])**3) <= (l[1]+l[2])**2:
        k += 1
print(k)
