n,m = [int(x) for x in input().rstrip().split(' ')]
A = [int(x) for x in input().rstrip().split(' ')]
A.sort()
S = 0
k = 0
for i in range(0, int(n/m)):
    k+=1
    S+=k*sum(A[i*m:(i+1)*m])

S+=k*sum(A[int(n/m)*m:])
print(int(S%1000000007))
