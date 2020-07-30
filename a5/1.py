'''
import itertools

def subset(inp):
    out = []
    for i in range(1, len(inp)+1):
    	k = list(map(list, itertools.combinations(inp, i)))
        for j in k:
        	if(j not in out):
	        	out.append(j)
    return out

def subset_sum(inp, rSum):
    out = []
    inp.sort()
    for i in subset(inp):
        if(sum(i)==rSum):
            out.append(i)
    return out
'''
from itertools import combinations 

def subset(inp):
    out = []
    for i in range(1, len(inp)+1):
        tmp = list(map(list, combinations(inp, i)))
        for j in tmp:
            if(j not in out):
                out.append(j)
    return out

def get_subset_for_sum(arr, k):
    # YOUR CODE HERE
    out = []
    arr.sort(reverse=True)
    for i in subset(arr):
        if(sum(i)==k):
            out.append(i)
    if(len(out)==1):
    	return out[0]
    return out
print get_subset_for_sum( [12, 1, 61, 5, 9, 2], 24)
