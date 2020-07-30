from random import randint
from sys import argv

alphabets = "abcdefghijklmnopqrstuvwxyz"

def getWord(letters: int) -> str:
	s = ""
	for i in range (letters):
		y = randint(0, 25)
	#	print(y),
		s += alphabets[y]
	return s

def readDictionary(letters):
	l = []
	f = open("words.txt", "r")
	#w = open("current.txt", "w")
	length = 0
	for word in f:
		if len(word) == letters + 1:
			length += 1
			l.append(word[:-1])
#			w.write(word)
	f.close()
	#w.close()
	
	return tuple(l), length

def compare(left, right):
	if left == right:
		return 0
	if left < right:
		return -1
	return 1

def isWord(allWords, length, word):
	left = 0
	right = length - 1
	
	while left <= right:
		mid = (left + right) // 2
		if compare(allWords[mid], word) == 0:
			return 1

		if compare(allWords[mid], word) < 0:
			left = mid + 1
		else:
			right = mid - 1
	
	return 0

#driver code
if __name__ == "__main__":
	argc = len(argv)
	if argc != 3:
		print ("Error: invalid arguments")
		exit(0)
	letters = int(argv[1])
	noOfWords = int(argv[2])
	tmp = noOfWords
	counter = 0
	iterations = 0
	allWords, length = readDictionary(letters)
	f = open("generated words.txt", "w")
	while noOfWords:
		counter += 1
		word = getWord(letters)
		f.write(word)
		if isWord(allWords, length, word):
			noOfWords -= 1
			print (counter, "\t", word)
			iterations += counter
			counter = 0
	print ("Average number of iterations:", iterations/tmp)
	print (" Total  number of iterations:", iterations)
	f.close()
	#print()
