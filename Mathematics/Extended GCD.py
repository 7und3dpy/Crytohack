"""def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)


gcd, u, v = extended_gcd(26513, 32321)
print(gcd,u,v)"""
# Source: https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
LARGE_NUM = 9999999
def extended_gcd(p,q):
    p0 = 0
    p1 = 1
    j = 0
    while j < LARGE_NUM:
        r_tmp = q % p #Remainder temp
        if (r_tmp == 0):
            break
        q_tmp = q // p #Quotient temp
        temp = (p0 - p1 * q_tmp) % 26
  
        p0 = p1
        p1 = temp

            
        q = p
        p = r_tmp
        j += 1
    return temp
print(extended_gcd(26513,32321))

'''
#In sage we have the 'xgcd' function
#The extended euclidean algorithm aims to find d =  gcd(a,b), and u, v given a, b
def extended_gcd(a,b):
    g,u,v = xgcd(a,b)
    print(g,u,v)
    print(u*a+v*b)
if __name__ == "__main__":
    extended_gcd(26513,32321)
'''
    
