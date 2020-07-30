import sys
def seq(n):
	#print n,
	if(n==4):
		return 4
	if(n%2==0):
		return (n/2)
	return (n*3+1)
def print_seq(n):
	print n,
	if (seq(n)==4):
		print "2 1"
		return 0
	return print_seq(seq(n))

n = int(sys.argv[1])
k = print_seq(n)
