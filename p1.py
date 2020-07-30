'''
from sys import argv
UNIT = "*"
CRLF = "\n"
SPACE = "-" 
SCREEN_WIDTH = 60 
def pattern(size: int, width = SCREEN_WIDTH): 
	return CRLF.join([ leading_space(line_no, width) + line(line_no) + leading_space(line_no, width) for line_no in range(size)]) 
def line(n: int) -> str: 
	return (UNIT+".")*n+UNIT
def leading_space(n: int, width: int) -> str: 
	return (width //2 - n) * SPACE 
print(pattern(int(argv[1]))) 
'''


from sys import argv 
STAR = "#"
CRLF = "\n" 
MINUS = "-" 
SPACE = " " 
SCREEN_WIDTH = 60 
SP = STAR 
RP = MINUS+MINUS
EP = "\b"+STAR
def pattern(size: int, width = SCREEN_WIDTH): 
 	return CRLF.join([line(line_no, width) for line_no in range(size)]) 
def line(n: int, width: int) -> str: 
 	return leading_space(n, width) + start_pattern(n) + repeat_pattern(n) + end_pattern(n)
def leading_space(n: int, w: int) -> str:
	return (w//2 - n) * SPACE 
def start_pattern(n: int): 
 	return SP 
def repeat_pattern(n: int): 
	return (n) * RP 
def end_pattern(n: int): 
	return EP 
print(pattern(int(argv[1]))) 
