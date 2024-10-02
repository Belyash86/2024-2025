#Запись в массив из текстового файла
l = [int(x) for x in open('17.txt')]

#Нахождение максимального элемента последовательности с условием.
#Например, макс. элемент, который делится на 3
print(max(x for x in l if x%3 == 0))


# перебор соседних пар
for i in range(len(l)-1):
    print(l[i], l[i+1])

print('------------')

# перебор соседних троек
for i in range(len(l)-2):
    print(l[i], l[i+1], l[i+2])

print('------------')

# перебор всех возможных пар
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        print(l[i], l[j])