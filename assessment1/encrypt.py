def encrypt(input_word):
    # YOUR CODE HERE
    d = {'a':0, 'e':1, 'o':2,'u':3}
    print d
    input_word = list((input_word)[::-1])
    print input_word
    for i in range(len(input_word)):
        if input_word[i].lower() in d:
            print i
            input_word[i] = str(d[input_word[i].lower()])
    print input_word
    return "".join(input_word)+"aca"

print encrypt("hello")
print encrypt("apple")
