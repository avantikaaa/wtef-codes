def getRow(row):
    # YOUR CODE HERE
    if(row<1):
        return 0
    if(row==1):
        return [1, 1]
    prev = getRow(row-1)
    out = []
    for i in range(row+1):
        if(i==0 or i==row):
            out.append(1)
        else:
            out.append(prev[i-1]+prev[i])
    return out
def pascals_triangle(row):
    # YOUR CODE HERE
    k = list(map(str, getRow(row)))
    print len(k)
    return " ".join(k)

print pascals_triangle(10)
print pascals_triangle(11)
print pascals_triangle(3)
print pascals_triangle(4)
