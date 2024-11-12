for A in range(50, 0, -1):
    f = 0
    for x in range(1, 100+1):
        for y in range(1, 100+1):
            f += (((x+y) <= 24) or (y<=x - 2) or (y >= A))
    if f == 100*100:
        print(A)
        break