def digits(n):
    if(n<10):
        return 1
    return 1+digits(n//10)

def perm(n):
    count = digits(n)
    p = pow(10, count-1)
    rotation = []
    for i in range (count):
        rotation.append(n)
        rem = n%10
        n = n//10
        n+= rem*p
    rotation.sort()
    return rotation

def prime(n):
    l = [True for i in range (n+1)]
    l[0] = False
    l[1] = False
    p = 2
    while(p*p<=n):
        if(l[p]==True):
            for i in range(p*p, n+1, p):
                l[i] = False
        p+=1
    return l

def isCircular(l, rotation):
    for i in rotation:
        print i
        if(l[i]==False):
            return False
    return True

def isCircularPrime(num):
    # YOUR CODE HERE
    rotation = perm(num)
    maximum = rotation[-1]
    print maximum
    return isCircular(prime(maximum), rotation)

print isCircularPrime(719)
