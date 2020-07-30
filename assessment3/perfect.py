from math import sqrt

N = 1000

def cubeRoot(left: int, right: int, cube: int)->int:
    if(left >= right):
        return right
    mid = (left + right)//2
    if(mid**3 == cube):
        return mid
    if(mid**3 > cube):
        return cubeRoot(left, mid-1, cube)
    return cubeRoot(mid+1, right, cube)

def cube_root(n: int)->int:
    return cubeRoot(0, n, n)

def isSqrt(n: int)->int:
    return sqrt(n) % 1 == 0

def limit(n: int)->int:
    print (n)
    return int(sqrt(N - n**3)) + 1

def qsqsq() -> [int]:
    # YOUR CODE HERE
    out = []
    print (cube_root(N))
    for i in range (1, cube_root(N)):
        for j in range (1, limit(i)):
            k = i**3 + j**2
            if isSqrt(k):
                out.append(k)
    out.sort()
    return out

print (qsqsq())
