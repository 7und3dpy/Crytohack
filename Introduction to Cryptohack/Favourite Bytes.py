u = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
a_ord = [o for o in bytes.fromhex(u)]
for i in range(256):
    possible_flag_ord = [i^o for o in a_ord]
    possible_flag = ''.join(chr(o) for o in possible_flag_ord)
    if possible_flag.startswith("crypto") == True:
        break
print(possible_flag)