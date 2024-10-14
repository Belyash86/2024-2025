l = [int(x) for x in open('2.txt')]
m41 = min([x for x in l if x>0 and x%41 == 0])
k = []
for i in range(len(l)-1):
    r = abs(l[i]-l[i+1])
    if (l[i] != l[i+1]) and r%m41 == 0:
        k.append(l[i]+l[i+1])
print(len(k), max(k))