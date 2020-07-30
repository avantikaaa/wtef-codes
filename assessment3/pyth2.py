from math import sqrt

N = 100

def gcd(m: int, n: int)->int:
    if(n==0):
        return m
    return gcd(n, m%n)

def GCD(a: int, b: int, c: int)->int:
    return gcd(a, gcd(b, c))

def isSqrt(n: int)->bool:
    return sqrt(n)%1==0

def limit(n: int)->int:
    return int(sqrt(N**2 - n**2)) + 1

def primitive_pyth() -> [(int, int, int)]:
    # YOUR CODE HERE
    out = []
    for a in range (1, N):
        for b in range(1, limit(a)):
            c = a**2 + b**2
            if(isSqrt(c)):
                if(GCD(a, b, sqrt(c)) == 1):
                    l = [a, b, int(sqrt(c))]
                    l.sort()
                    l = tuple(l)
                    if not l in out:
                        out.append(l)
    return out
    
print (primitive_pyth())
