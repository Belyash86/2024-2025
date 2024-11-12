from ipaddress import ip_network
k = 0
for ip in ip_network('115.192.0.0/255.192.0.0'):
    if f'{ip:b}'.count('1') % 3 > 0:
        k += 1
print(k)