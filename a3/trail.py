def trail(n, p):
    if(n//p==0):
        return 0
    return n//p+trail(n, p*5)

print trail(4, 5)
print trail(5, 5)
print trail(10, 5)
print trail(17, 5)
print trail(25, 5)
