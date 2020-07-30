from sys import argv

def expand(num: int)-> str:
    # YOUR CODE HERE
    out = []
    tenthPlace = 1
    while(num > 0):
        tmp = num % 10
        if(tmp != 0):
            out.append(str(tmp * tenthPlace))
        num //= 10
        tenthPlace *= 10
    out.reverse()
    return " + ".join(out)

print (expand(int(argv[1])))
