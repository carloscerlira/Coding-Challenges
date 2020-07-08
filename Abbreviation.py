def Abbreviation(a,b):
    dp = [[] for x in range(len(b))]
    for i in range(len(b)):
        for j in range(len(a)):
            dp[i].append(0)
    
    dp[0][0] = 1

    for j in range(1,len(a)):
        if a[j].islower():
            dp[0][j] = dp[0][j-1]

    for i in range(1,len(b)):
        for j in range(1,len(a)):
            if a[j].isupper():
                if(a[j]==b[i]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 0
            else:
                if a[j].upper() == b[i]:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
    
    # print(a,b)
    # print(dp)
    if dp[-1][-1] == 1:
        print('YES')
    else:
        print('NO')

# a,b = "AbCdE", "AFE"
# a = a[a.upper().index('A'):]
# Abbreviation(a,b)

q = int(input())
for i in range(q):
    a = input()
    b = input()
    if b[0] not in a.upper():
        print('NO')
    else:
        a = a[a.upper().index(b[0]):]
        Abbreviation(a,b)
