def quad_resi(p,l): #p mean integer p, l is the list of the ints
    res = []
    for num in l:
        for a in range(1,p):    
            if a**2 % p == num:
                res.append(a)
    return min(res)

print(quad_resi(29, [14, 6, 11]))