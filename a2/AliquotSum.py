import math
def aliquotSum(n):
	out = 0
	for i in range(2, int(math.sqrt(n)) + 1):
		if(n%i==0):
			out+=i
			out+=n/i
	return out+1

def classify(n):
	return ["Beta", "Gamma", "Alpha"][cmp(n, aliquotSum(n))+1]

a = classify
print a(6), a(12), a(5)
