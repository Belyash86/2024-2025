def is4(x): return len(str(abs(x))) == 4
k = []
l = [int(x) for x in open('files/17.txt')]
max39 = max([int(x) for x in l if x>0 and is4(x) and str(x)[-2:] == '39'])
for x,y in zip(l, l[1:]):
    if ((is4(x) and is4(y) == False) or (is4(x) == False and is4(y))) and (x+y)**2 <= max39**2:
        k.append(x+y)
print(len(k), max(k))