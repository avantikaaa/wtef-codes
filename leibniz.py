#Change the code-> Function should only find the value, not return the error in the value
def liebniz(n):
	p = 0.7853981633974483
	k = 1.0
	out = 0
	for i in range (n):
		out += k/((2*i)+1)
		k  *= (-1)
	out = out/4
	return abs(out-p)

#driver code
n = input()
out = liebniz(n)
print (out)
