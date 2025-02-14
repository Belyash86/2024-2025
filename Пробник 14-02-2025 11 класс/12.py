for n in range(2, 100, 2):
    s = '>2'+'12'*n+'<'
    while '>2<' not in s:
        s = s.replace('>1', '>2', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('1<', '<2', 1)
    s = s.replace('<','').replace('>','')
    if sum([int(x) for x in s]) > 103:
        print(n)
        break
