from math import prod
k = []
l = [int(x) for x in open('files/3.txt')]
m09 = max([x for x in l if str(x)[-2:] == '09'])
for i in range(len(l)-2):
    tr = l[i:i+3]
    if (len([x for x in tr if x%7 == 0])) == 2 and sum(tr) < m09: k.append(prod(tr))
print(len(k), min(k))