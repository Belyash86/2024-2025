from itertools import product
i = 1
for p in product('АЙЛМ', repeat = 5):
    s = ''.join(p)
    if s.count('М') == 0 and s.count('Л') == 0 and 'ЙЙ' not in s:
        print(i, s)
    i += 1