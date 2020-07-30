from sys import argv

def look_and_say(n: int)->str:
    # YOUR CODE HERE
    n = str(n)
    print (n)
    out = ""
    i = 0
    while(i < len(n) - 1):
        out += n[i + 1] * int(n[i])
        i += 2
    return out

print(look_and_say(int(argv[1])))
