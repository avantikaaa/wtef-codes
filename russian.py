import sys
def russian(a,b):
    if(a>b):
        (a,b) = (b,a)
    s = ""
    l1 = len(str(a))+1
    l2 = len(str(b))+1
    out = 0
    while(a>0):
        s = s+ str(a).rjust(l1, " ")+" "+str(b).rjust(l2, " ")
        if(a%2!=0):
            out+=b
            s+=" +"
        b *= 2
        a = a//2
        s+="\n"
    s+="".rjust(l1+l2*2, "=")+"\n"
    s+="".rjust(l1+1, " ")+str(out)+"\n"
    s+="".rjust(l1+l2*2, "=")
    return s
print russian(int(sys.argv[1]), int(sys.argv[2]))

