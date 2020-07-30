def sortedTuple(word):
	return tuple(sorted(i for i in word))

def isAnagram(out, word):
	w = sortedTuple(word)
	if w not in out:
		out[w] = []
	out[w].append(word)

def groupAnagram(words):
	out = {}
	for word in words:
		isAnagram(out, word.lower())
	return sorted([out[i] for i in out])
