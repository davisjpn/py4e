def gcdIter(a,b):
    r = min(a,b)
    gcd = ""
    for i in range(1,r+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd

print(gcdIter(9,12))
