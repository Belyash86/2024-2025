l = [int(x) for x in open('6643-kp.txt')]
max1001 = max([abs(x) for x in l if x%1001 == 0])
k, min_sum = 0, 10**20
for i in range(len(l)-1):
    if (len(str(abs(l[i]))) == 3 or len(str(abs(l[i+1]))) == 3) and (l[i]+l[i+1]) > max1001:
        k += 1
        min_sum = min(min_sum, l[i]+l[i+1])
print(k, min_sum)