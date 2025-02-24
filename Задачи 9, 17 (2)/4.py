k = []
l = [int(x) for x in open('files/4.txt')]
m50 = max([x for x in l if str(x)[-2:] == '50'])
for i in range(len(l)-2):
    tr = l[i:i+3]
    tr5 = [x for x in tr if 9999<abs(x)<100000]
    if len(set(tr5)) == 3 and sum(tr) <= m50: k.append(sum(tr))
print(len(k), max(k))