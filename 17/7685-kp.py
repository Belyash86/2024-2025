def nod(x, y):
    while x != y:
        if x>y: x -= y
        else: y -= x
    return x

l = [int(x) for x in open('7685-kp.txt')]
nods = [0]*1000
for i in range(len(l)-1):
    nods[nod(l[i], l[i+1])] += 1
n = nods.index(max(nods))
max_sum = 0
for i in range(len(l)-1):
    if nod(l[i], l[i+1]) == n:
        max_sum = max(max_sum, l[i]+l[i+1])
print(n, max_sum)