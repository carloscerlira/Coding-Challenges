def extraLongFactorials(n):
    factorials = []; factorials.append(1)
    for i in range(1, n+1):
        factorials.append(i*factorials[i-1])

    return factorials[-1]


print(extraLongFactorials(25))