from math import sqrt
N = 1000

def isSqrt(n: int)->int:
	return sqrt(n) % 1 == 0

def allTriads(n: int):
	out = []
	for a in range (1, n):
		for b in range (a, n):
			c = a**2 + b**2
			if(isSqrt(c)):
				if(a + b + sqrt(c) <= n):
					out.append([a, b, int(sqrt(c))])
#	print (out)
	return out

def peri() -> int:
	out = [0] * (N + 1)
	for i in allTriads(N):
		out[sum(i)] += 1
	return out.index(max(out))

print (peri())
