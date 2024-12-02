from fnmatch import fnmatch
for i in range(0, 10**10, 8993):
    if fnmatch(str(i), '89*4?5?7?'):
        print(i, i//8993)