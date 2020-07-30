def isValid(n):
	l = [int(i) for i in str(n)]
	length = len(l)
	if(length>9):
		return -1

	s = 1
	e = 9
	first = ""
	last = ""
	for i in range (length):
		first = first+ str(s)
		last = str(e) + last
		e-=1
		s+=1
	first = int(first)
	last = int(last)

	if(n>last):
		return first
	
	for i in range (length-1, 0, -1):
		if(l[i]<=l[i-1]):
			j = i
			while(j<length):
				while(l[j]<=l[j-1]):
					if(l[j]==9
				j+=1
					
