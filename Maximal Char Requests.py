def maximal(S):
    C.append([S.count(x) for x in abc])
    
abc = 'abcdefghijklmnopqrstuvwxyz'
N = int(input())
S = input()
S = S.lower()
Q = int(input())

A = []
C = []
I = []
for i in range(Q):
    s,f = [int(x) for x in input().split(' ')]
    I.append([s,f])
    A.append(s); A.append(f)

A.sort()
A = list(set(A))

for i in range(len(A)-1):
    s,f = A[i],A[i+1]
    maximal(S[s:f+1])

for k in range(len(I)):
    s,f=I[k][0],I[k][1]
    if(s==f):
        print(1)
        continue;
    s,f = A.index(s), A.index(f)
    R = [0 for x in abc]
    for i in range(s,f):
        #print(S[A[i+1]])
        for j in range(len(R)):
            R[j] += C[i][j] 
        
        if(i+1 != f):
            index = abc.index(S[A[i+1]])
            R[index] -= 1

    for i in range(len(R)-1,-1,-1):
        if(R[i] != 0):
            print(R[i])
            break;


    