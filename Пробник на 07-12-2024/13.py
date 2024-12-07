from ipaddress import ip_network
k = 0
for ip in ip_network('172.30.0.0/255.254.0.0'):
    if f'{ip:b}'.count('1') % 12 != 0: k += 1
print(k)