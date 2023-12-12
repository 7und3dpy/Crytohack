

a = 66528
b = 52920

"""while a>b:
    q = a//b
    r = a%b
    if r==0:
        print(b)
        break
    a=b
    b=r"""
def the_gcd(a,b):
    #If a<b: swap them
    if a < b:
        a,b = b,a
    #If we encounter 0, return a
    if b == 0:
        return a
    else:
        r = a % b
        return the_gcd(b,r)
print(the_gcd(a,b))

"""
Implementation Pseudocode

function gcd(a,b)
    while b != 0
        t:=b
        b:=a mod b
        a:=t

Other version but having minus operator

function gcd(a,b)
    while a != b   
        if a > b
            a:= a - b
        else
            b:= b - a
    return 0

The recursive version

function gcd(a,b)
    if b = 0 
        return a
    else
        return gcd(b, a mod b)
        
"""