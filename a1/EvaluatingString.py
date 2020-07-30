def checkPossible(string):
	if(ord(string[0])>ord('2')):
		return False
	if(ord(string[len(string)-1])>ord('2')):
		return False
	c = False
	for i in range (1, len(string)-1):
		if(ord(string[i])>50):
			c = True
		if(ord(string[i])>ord('2') and ord(string[i+1])>ord('2')):
			return False
		if(ord(string[i])>ord('2') and ord(string[i-1])>ord('2')):
			return False
	return c
	
def binToDec(string):
	out = 0
	for i in string:
		out *=2
		out += int(i)
	return out

def convert(num1, num2, func):
	if(func=='A'):
		return (num1&num2)
	if(func=='B'):
		return (num1|num2)
	return (num1^num2)

def Evaluating_String(string):
	if not checkPossible(string):
		return -1
	str1 = ""
	i = 0
	while(ord(string[i])<50):
		str1 += string[i]
		i += 1
	num1 = binToDec(str1)
	out = 0
	while(i<len(string)):
		char = string[i]
		i+=1
		str2 = ""
		while(i<len(string) and ord(string[i])<50):
			str2+=string[i]
			i += 1
		num2 = binToDec(str2)
		num1 = convert(num1, num2, char)
	return num1
