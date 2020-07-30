from sys import argv

def kempner(n):
    # YOUR CODE HERE
    fact = 1
    i = 0
    while (fact % n != 0):
        i += 1
        fact *= i
    return i

print (kempner(int(argv[1])))
