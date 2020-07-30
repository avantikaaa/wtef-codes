from sys import argv
def compressString(s):
	count = 0
	s+="!"
	letter = s[0]
	out = ""
	for i in s:
	   if(letter==i):
	        count+=1
	   else:
	       if(count>2):
    	           out+=str(count)+letter
	       else:
	           out+=letter*count
	       count = 1
	       letter=i
	return out
print compressString(argv[1])	
