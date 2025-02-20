def to3(x):
    ans = []
    while x:
        if x%3 == 2: ans.append(2)
        x //= 3
    return sum(ans)
l = [int(x) for x in open('files/3.txt')]
s60 = sum([to3(x) for x in l if x%60 == 0])
k = []
for x, y in zip(l, l[1:]):
    if x>s60 or y>s60: k.append(x+y)
print(len(k), max(k))