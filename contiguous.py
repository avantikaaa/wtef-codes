def contiguous(string):
	length = len(string)
	i=0
	while(i<length and string[i]=='0'):
		i+=1
	if (i==length):
		return 0
	start = i
	i = length-1
	while(i>start and string[i]=='0'):
		i-=1
	end = i
	count = 0
	for i in range (start, end, 1):
		if(string[i]=='0'):
			count +=1
	return count
def zero(string):
	return string.strip("0").count("0")
	
string = raw_input()
print contiguous(string)
print zero(string)
