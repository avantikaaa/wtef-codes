def gcd(m: int, n: int)->int:
    if(n==0):
        return m
    return gcd(n, m%n)

print (gcd(500, 30))
