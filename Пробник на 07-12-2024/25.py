from fnmatch import fnmatch
for i in range(0, 10**10, 96437):
    if fnmatch(str(i), '7?2*4??9?'):
        print(i, i//96437)