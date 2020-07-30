s = input()
alph = [0]*26
for i in s:
	alph[ord(i)-97]  = 1
n = int(input())
for i in range(n):
	out = "Yes"
	word = input()
	for c in word:
		if alph[ord(c)-97] == 0:
			out = "No"
			break
	print (out)
