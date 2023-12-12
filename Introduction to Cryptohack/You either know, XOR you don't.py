u = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104' #consider it as message
v = bytes.fromhex(u)
#since we know that 'crypto{' is the partial flag
"""
we have message ^ secret_key = flag
    and message[:7] ^ partial_secret_key = partial_flag
    ==> partial_secret_key = message[:7]^partial_flag
"""
flag = []
se_key = [a^b for a,b in zip(v[:7],b'crypto{')]+[ord('y')]  #since we print to b'myXORke', guess after that it's y, 
for i in range(len(v)):
    flag.append(v[i]^se_key[i % len(se_key)])
    
print(''.join(chr(i) for i in flag))