'''
Introduce Fermat's little theorem

Fermat`s little theorem states that if p is a prime number, then for any integer a, the number a^p - a is an integer multiple of p.

Here p is a prime number

a^p  = a (mod p)

Special Case: If a is not divisible by p, Fermat's little theorem is equivalent to the statement that a^(p-1)-1 is an integer multiple of p. 

a^(p-1) = 1 (mod p)

OR a**(p-1) % p = 1

Here a is not divisible by p

Use fermat's little theorem

a^(m-1) = 1 (mod m)

=> a^(-1) = a^(m-2) (mod m)

'''
a = 3
m = 13
print(pow(a,m-2,m))
#print(pow(3,-1,13))