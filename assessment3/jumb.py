from sys import argv
def pick10(s: str, n:int) -> str:
    # YOUR CODE HERE
    out = ""
    count = 0
    l = len(s)
    for i in range (10):
        out += s[(n + count)%l]
        count += i+1
    return out

print (pick10(argv[1], int(argv[2])))
