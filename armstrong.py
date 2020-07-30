def is_armstrong(n):
	l = []
	num = n
	while(n>0):
		l.append(n%10)
		n = n/10
	if(sum(l)==num):
		return True
	return False

def nearestArmstrongNumber(n):
	while not is_armstong(n):
		n+=1
	return n

