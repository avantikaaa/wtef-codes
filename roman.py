from sys import argv

def romanToInt(string):
    string = string.lower()
    string  += 'i'
    numerals = {'i': 1, 'v': 5, 'x': 10, 'l':50, 'c': 50, 'd': 500, 'm': 1000}
    integer = 0
    for i in range (len(string)-1):
        if (numerals[string[i]] < numerals[string[i+1]]):
            integer -= numerals[string[i]]
        else:
            integer += numerals[string[i]]
    return integer

print (romanToInt(argv[1]))

