from math import ceil
f = open('files/26.txt')
k, n = map(int, f.readline().split())
l = sorted([[int(x) for x in s.split()] for s in f])
domiki, max_line = [0]*1000, 0
for chel in l:
    for d in range(len(domiki)):
        if chel[0] > domiki[d]:
            domiki[d] = chel[1]
            max_line = max(max_line, ceil(len([x for x in domiki if x >= chel[0]])/k))
            break
print(max_line, len([x for x in domiki if x > l[-1][0]]))