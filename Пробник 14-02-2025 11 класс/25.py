from fnmatch import fnmatch
ans = []
for i in range(0, 10**9, 7863):
    if fnmatch(str(i), '?54*32*1'):
        ans.append([i, sum([int(x) for x in str(i)])])
for n in sorted(ans, key = lambda x: (x[1], x[0])): print(*n)