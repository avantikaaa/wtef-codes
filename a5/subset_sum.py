#DO NOT TOUCH THIS CODE. 
def subsetSum(inp, rSum, out, out1):
    #print sum(out), out
    add = sum(out)
    if(add == rSum):
    #    print "1", out
        out1.append(out)
    #    print out1
        return
    if(add > rSum):
        return
    else:
        out.append(inp[0])
      #  print inp[1:]
        for i in range(1, len(inp)):
#	'''
 #       DOESN'T WORK IF THE LAST ELEMENT IS PART OF THE SUM AS IT DOESN'T ENTER THIS LOOP: solution-> append 0.
    #    why isn't pass by reference working.
	#'''
            subsetSum(inp[i:], rSum, out, out1)
        out.pop()

def subset_sum(inp, rSum, out1):
    if(len(inp) == 0):
        return out1
    for i in range (len(inp)):
        if(inp[i] <= rSum):
            subsetSum(inp[i:], rSum,[], out1)
    #return subset_sum(inp[1:], rSum, out1)
    return out1

print subset_sum([61, 9, 12, 5, 1, 4, 2, 0], 24, [])
