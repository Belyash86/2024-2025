l = [int(x) for x in open('files/17.txt')]
ans = []
max42 = max([x for x in l if str(x)[-2:] == '42' and len(str(abs(x))) == 4])

for i in range(len(l)-2):
    tr = l[i:i+3]
    cond1 = len([x for x in tr if str(x)[-2:] == '42' and len(str(abs(x))) == 4]) >= 2
    cond2 = sum(tr) > max42
    if cond1 and cond2: ans.append(sum(tr))
print(len(ans), max(ans))
