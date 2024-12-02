#from fnmatch import fnmatch
# def is_prime(n):
#     if any(n%i == 0 for i in range(2, int(n**0.5)+1)):
#         return False
#     return True

# for i in range(301111, 10**7+1):
#     if is_prime(i) and fnmatch(str(i), '3?1111*'):
#         print(i)

def is_prime(n):
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

for i in range(10):
    for j in range(10): #По условию задачи макс. число = 10**7, то есть вместо * возожно подставить только числа диапазона 0..9
        d = int(f'3{i}1111{j}')
        if is_prime(d):
            print(d)