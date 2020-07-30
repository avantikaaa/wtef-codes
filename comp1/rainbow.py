def check(a, n):
	count = [0]*7
	prev = 0
	i = 0
	for i in range (n):
#		print (a[i])
		if(a[i] > 7):
#			print("A")
			return False
		if a[i] == 7:
			break
		if (a[i] == prev) or (a[i] == prev + 1):
			count[a[i]-1] += 1
		prev = a[i]

#	print(count)

	while i<n:
#		print(a[i])
		if a[i] == 7:
			i += 1
		else:
			count[a[i]-1] -= 1
			if count[a[i]-1] < 0:
#				print(count)
#				print("B")
				return False
			i += 1
	return True
	
test = int(input())
for t in range (test):
	n = int(input())
	arr = list(map(int, input().split()))
	if check(arr, n):	
		print("yes")
	else:
		print("no")
