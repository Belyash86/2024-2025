l = [int(x) for x in open('files/17.txt')]
min41 = min([x for x in l if x > 0 and x%41 == 0])
k, max_sum = 0, -10**10
for i in range(len(l)-1):
    if (l[i] != l[i+1]) and (abs(l[i] - l[i+1]) % min41 == 0):
        k += 1
        max_sum = max(max_sum, l[i] + l[i+1])
print(k, max_sum)