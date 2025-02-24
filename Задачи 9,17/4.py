l = [int(x) for x in open('files/4.txt')]
m22 = max([x for x in l if len(str(abs(x))) == 4 and str(x)[-2:] == '22'])
k = []
for i in range(len(l)-2):
    c = l[i:i+3]
    if len(set([len(str(abs(x))) for x in c])) == 3 and sum(c) >= m22:
         k.append(sum(c))
print(len(k), max(k))