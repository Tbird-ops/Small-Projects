import random as rand

chars = '0123456789abcdef'
file = open('macaddr.txt', 'w')

x = int(input("Enter the number of mac addresses: "))

for i in range(x):
    addr = ''
    for x in range(12):
        char = chars[rand.randint(0,15)]
        addr += char
        if(x%2 == 1 and x!= 0 and x!=11):
            addr += ':'
    addr += '\n'
    file.writelines(addr)


file.close()