def check(arr, n):
	if arr[1] - arr[0] != 1:
		return arr[0]
	for i in range (1, n):
		if arr[i] - arr[i-1] != 1:
			return arr[i]

test = int(input())
for t in range (test):
	n = int(input())
	arr = input()
	arr = list(map(int, arr.split()))
	arr.sort()
	print(check(arr, n))
