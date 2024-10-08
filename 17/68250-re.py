l = [int(x) for x in open('68250-re.txt')]
k, max_sum = 0, 0
m538 = max([x for x in l if str(x)[-3:] == '538'])
for i in range(len(l)-3):
    c = l[i:i+4]
    u1 = 2 <= [len(str(x)) for x in c].count(5) < 4
    u2 = len([x for x in c if x%3 == 0]) > len([x for x in c if x%7 == 0])
    u3 = m538 < sum(c) < m538*2
    if u1 and u2 and u3:
        k += 1
        max_sum = max(max_sum, sum(c))
print(k, max_sum)