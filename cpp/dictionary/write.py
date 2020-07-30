f = open("words.txt", "r")
w = open("all.txt", "w+")

l = []
for word in f:
    l.append(word[:-1])
for word in l:
    w.write(word)
    w.write(" ")

f.close()
w.close()
