def fizzbuzz(n):
	s = ""
	if(n%3==0):
		s+="Fizz"
	if(n%5==0):
		s+="Buzz"
	if(s==""):
		s = str(n)
	return s
