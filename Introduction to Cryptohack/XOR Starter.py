u = 'label'
h=''
for x in u:
    a=''
    b=''
    a+=str(ord(x))
    b+=str(int(a)^13)
    h+=chr(int(b))
print(h)

    
