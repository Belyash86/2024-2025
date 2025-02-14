l  = [len(s) for s in open('files/24.txt').readline().split('Z')]
print(min(sum(l[i:i+119])+120 for i in range(1, len(l)-120)))
# Минимальная строка, содержащая 120 Z,
# начинается и заканчивается буквой Z
# и содержит 119 подстрок между остальными Z