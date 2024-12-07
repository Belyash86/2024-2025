for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = c and (a or d) and (d <= b)
                if f:
                    print(b,c,a,d)