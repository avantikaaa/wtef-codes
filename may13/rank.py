import itertools as it
import os
from sys import argv 

def relation(A, B):
	metric = sum([int(a > b) for a, b in zip(A, B)])
	if metric == len(A):
		return ">"
	elif metric == 0:
		return "<"
	else:
		return "#"

#what is line? wasn't defined before this.
def createDict(filename) -> dict:
	matrix = {}
	for line in open(filename):
		marks = line.strip().split()
		matrix[marks[0]] = [int(x) for x in marks[1:]]
	return matrix

def allRelations(matrix: dict) -> set:
	keys = list(matrix.keys())
	combo = it.combinations(keys, 2)
	rels = set([])
	for key1, key2 in combo:
		r = relation(matrix[key1], matrix[key2])
		if r == ">":
			rels.add(key1 + key2)
		elif r == "<":
			rels.add(key2 + key1)
	
	return list(sorted(rels))

def remove(rels):
	start = set([x[0] for x in rels])
	end = set([x[1] for x in rels])
	both = start & end
	
	removables = set([])
	rules = set([])
	
	for x in start:
		for y in end:
#			if x + y not in rels:
	#			continue
			for z in both:
				if x + z in rels and z + y in rels:
					removables.add(x+y)
					rules.add(x+y + " <= " + x+z + " & " + z+y)
	return (list(sorted(removables)), list(sorted(rules)))

def minimal(rels, removables):
	return sorted(set(rels) ^ removables)

def finalRelation(mini):
	out = []
	for i in mini:
		flag1 = 0
		flag2 = 0
		for j in range (len(out)):
			if out[j][0] == i[-1]:
				out[j] = i[0] + out[j]
				flag1 = 1
				flag2 += 1
				break
			elif out[j][-1] == i[0]:
				out[j] = out[j] + i[-1]
				flag1 = 1
				flag2 += 1
				break
		if flag1 == 0:
			out.append(i)
	if flag2 == 0:
		return out
	return finalRelation(out)

def main():
	matrix = createDict(argv[1])
	rels = allRelations(matrix)

	print("All relations:\n\t", rels)
	
	removables, rules = remove(rels)
		
	print("Removables\n\t", list(removables))
#	print("Removable Rules:\n\t", rules)
	
	mini = minimal(rels, set(removables))

	print("Minimal\n\t", mini)
	
	output = finalRelation(mini)
	
	print("Final:\n\t", output)

main()
