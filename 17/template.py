#Запись в массив из текстового файла
l = [int(x) for x in open('17.txt')]

# перебор соседних пар
for i in range(len(l)-1):
    print(l[i], l[i+1])

print('------------')

for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        print(l[i], l[j])