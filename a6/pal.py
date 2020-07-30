from collections import Counter
from sys import argv
def palindrom(word):
    letters = dict(Counter(word))
    count = 0
    for i in letters:
    	if(letters[i]%2 == 1):
    		count += 1
    	if(count == 2):
    		return False
    return True
print palindrom(argv[1])
