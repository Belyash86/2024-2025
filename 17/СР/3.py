l = [int(x) for x in open('1.txt')]
m = min(l)

k, min_sum = 0, 10**20
for i in range(len(l)-1):
    if l[i]%55 == m or l[i+1]%55 == m:
        k += 1
        min_sum = min(min_sum, l[i]+l[i+1])
print(k, min_sum)