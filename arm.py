import sys
def arm(a, b):
    return [i for i in range(a,b) if isArm(i, digits(i))]
def digits(n):
    c = [int(ch)**3 for ch in str(n)]
    return sum(c)
def isArm(n, s):
    return n==s
a, b = int(sys.argv[1]), int(sys.argv[2])
print arm(a, b)
