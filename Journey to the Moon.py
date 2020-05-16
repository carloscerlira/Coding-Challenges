def journeyToTheMoon(A):
    return 0;

# n, p = [int(x) for x in input().split(' ')]
n, p = 4, 5
A = [[1,2],[2,4],[5,3],[5,6],[6,1]]
A.sort(key=lambda x: x[0])
A = A[::-1]
print(A)
C = []; C.append(A[0])
for i in range(1,p):
    # a1, a2 = [int(x) for x in input().split(' ')]
    a1, a2 = A[i]
    for j in range(len(C)):
        if a1 in C[j]:
            if a2 not in C[j]:
                C[j].append(a2)
            break;
        if a2 in C[j]:
            if a1 not in C[j]:
                C[j].append(a1)
            break;
        if(j == len(C)-1):
            C.append([a1, a2])
print(C)
    