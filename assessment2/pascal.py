def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

def nCr(n, r):
    n1 = fact(n)
    r1 = fact(r)
    k = fact(n-r)
    return(n1/(k*r1))

def pascals_triangle(row):
    # YOUR CODE HERE
    out = []
    for i in range(row+1):
        out.append(str(nCr(row, i)))
    return " ".join(out)

print pascals_triangle(10)
print pascals_triangle(11)
print pascals_triangle(3)
print pascals_triangle(4)
