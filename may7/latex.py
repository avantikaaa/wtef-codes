from sys import argv

def readFile(filename: str) -> str:
	f = open(filename, "r")
	equation = f.read()
#	print (equation)
#	equation.strip("$")
#	print (equation)
	f.close()
	return equation[1: -2]

def editEquation(equation: str) -> str:
	if equation[0] != "-":
		equation = "+ " + equation
	return equation

def toGeneralForm(equation: str) -> str:
	eq = equation.split(" ")
	out = []

	while eq != [] :
		out.append(eq[-2])
		out.append(eq[-1])
		eq.pop()
		eq.pop()

	if out[0] == "+":
		out.pop(0)
	return "$" + " ".join(out) + "$"

fileName = argv[1]
equation = readFile(fileName)
equation = editEquation(equation)
#print (equation)
print (toGeneralForm(equation))
