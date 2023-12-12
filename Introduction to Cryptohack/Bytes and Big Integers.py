from Crypto.Util.number import *
u = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(u))

'''
for example
from Crypto.Util.number import *
a = "HELLO"
b = ''
for x in a:
    b += str(ord(x))
c = bytes(b,'utf-8')
print(c)
print(bytes_to_long(c))
'''