from ipaddress import ip_network
k = 0
for ip in ip_network('112.160.0.0/255.240.0.0'):
    if f'{ip:b}'.count('1') % 5 == 0:
        k += 1
print(k)