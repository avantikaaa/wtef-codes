def SplitParenthesis(txt)-> [str]:
    # YOUR CODE  HERE
    stack = []
    out = []
    tmp = ""
    balance = {')': '(', ']': '[', '}': '{'}
    for i in txt:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
            tmp = tmp + i
        elif stack[-1] == balance[i]:
            tmp = tmp + i
            stack.pop()
            if len(stack) == 0:
                out.append(tmp)
                tmp = ""
    return out

print (SplitParenthesis("()()()"))
print (SplitParenthesis("((()))"))
print (SplitParenthesis("((()))(())()()(()())"))
print (SplitParenthesis("((())())(()(()()))"))
