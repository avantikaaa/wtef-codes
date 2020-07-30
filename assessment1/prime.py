def isPrime(n):
    for i in range(2, n):
        if(n%i==0):
            return False
    return True
def getPrimoral(number):
    # YOUR CODE HERE
    i = 0
    prod = 1
    prime = 2
    while(i<number):
        while not isPrime(prime):
            prime+=1
        prod *= prime
	prime +=1
        i += 1
    return prod

print getPrimoral(1)
print getPrimoral(4)
print getPrimoral(3)
print getPrimoral(5)
