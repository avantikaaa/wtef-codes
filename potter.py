import math
def all_even(n):
	while(n>0):
		if (n%2==1):
			return False
		n = n//10
	return True

def is_sqrt(n):
	return math.sqrt(n)%1==0

def potter(n):
	return all_even(n) and is_sqrt(n)

def print_potter():
	for i in range(1000, 10000):
		if(potter(i)):
			print i,
	print ""
print_potter()
