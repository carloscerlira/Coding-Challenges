def arrayManipulation(I):
    a, b, k = I
    for i in range(a-1, b):
        A[i] += k

n,m = [int(x) for x in input().split(' ')]
A = [0 for i in range(0,n)]

for i in range(0,m):
    arrayManipulation([int(x) for x in input().split(' ')])

print(max(A))