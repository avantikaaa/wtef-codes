def string_match(s1, s2):
    count = 0
    for i in range (len(s1)):
        if(s1[i]==s2[i]):
            count+=1
    return count

def matches(s1, s2):
    if(len(s1)<len(s2)):
        return string_match(s1, s2)
    return string_match(s2, s1)

print matches("HELLO", "OLLEH")
