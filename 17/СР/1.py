l = [int(x) for x in open('1.txt')]
k2 = len([x for x in l if len(str(x)) == 2])

k, min_sum = 0, 10**20
for i in range(len(l)-1):
    if (l[i]%10 + l[i+1]%10) == k2:
        k += 1
        min_sum = min(min_sum, l[i]+l[i+1])
print(k, min_sum)