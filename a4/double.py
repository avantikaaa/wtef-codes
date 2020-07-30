def binary(n):
    s = ""
    while(n>0):
        s = str(n%2)+s
        n = n//2
    return s

def isPalindrome(string):
    l = len(string)-1
    for i in range(0, (l+1)//2):
        if(string[i]!=string[l-i]):
            return False
    return True

def isDoubleBasePalindrome(n):
    #YOUR CODE HERE
    return isPalindrome(str(n)) and isPalindrome(binary(n))
print isDoubleBasePalindrome(5)
print isDoubleBasePalindrome(58)
