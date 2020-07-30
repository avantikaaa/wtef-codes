def changeChar(c, word, case):
	w  = [i for i in word]
	vowel = ['a', 'e', 'i', 'o', 'u']
	if(case=='vowel'):
		for i in range (len(w)):
			if w[i].lower() in vowel:
				w[i] = c
	else:
		for i in range (len(w)):
			if not w[i].lower() in vowel:
				w[i] = c
	return "".join(w)
def stringTransformation(array):
	array[0] = changeChar('$', array[0], 'vowel')
	array[1] = changeChar('#', array[1], 'cons')
	array[2] = array[2].upper()
	return "".join(array)
