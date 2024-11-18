l = [int(x) for x in open('files/17.txt')]
min8 = min([x for x in l if x%10 == 8])
k = []
for i in range(len(l)-1):
    if ((l[i] % 16 == min8) and (l[i+1] % 16 != min8)) or ((l[i] % 16 != min8) and (l[i + 1] % 16 == min8)):
        k.append(l[i]+l[i+1])
print(len(k), max(k))
