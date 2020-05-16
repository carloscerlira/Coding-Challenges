def balancedBrackets(S):
    dic = {'}':'{',']':'[',')':'('}
    stack = []

    for s in S:
        if(s in dic.values()):
            stack.append(s)
        if(s in dic.keys()):
            if len(stack) != 0 and stack[-1] == dic[s]:
                stack.pop()
                continue;
            else:
                return 'NO'
    if len(stack) == 0:
        return  'NO'
    return 'YES'

n = int(input())
for i in range(n):
    s = input()
    print(balancedBrackets(s))
