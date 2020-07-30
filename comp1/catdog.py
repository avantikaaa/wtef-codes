def minimum(c, d):
	if(c <= d*2):
		return d
	return (c+d)

def check(c, d, l):
	m = minimum(c, d)
	return (m*4 <= l) and (l <= (c+d)*4) and (l%2 == 0)

t = int(input())
for test in range (t):
	c, d, l = map(int, input().split())
	if check(c, d, l):
		print("yes")
	else:
		print("no")
