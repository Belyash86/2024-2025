s = open('files/24.txt').readline()
k, k_max = 1, 0
for i in range(len(s) - 1):
    if (s[i] == 'S' and s[i+1] == 'Q') or (s[i] == 'Q' and s[i+1] == 'R') or (s[i] == 'R' and s[i+1] == 'P') or (s[i] == 'P' and s[i+1] == 'S'):
        k += 1
        k_max = max(k, k_max)
    else:
        k = 1
print(k_max)