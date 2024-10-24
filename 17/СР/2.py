l = [int(x) for x in open('2.txt')]
m41 = min([x for x in l if x>0 and x%41 == 0])
k, max_sum = 0, 0
for i in range(len(l)-1):
    r = abs(l[i]-l[i+1])
    if (l[i] != l[i+1]) and r%m41 == 0:
        k += 1
        max_sum = max(max_sum, l[i]+l[i+1])
print(k, max_sum)