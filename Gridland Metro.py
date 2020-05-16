from bisect import bisect

# X = [1,6,7,20,23,39]
# print(X)
# c1, c2 = [7,12]

# i1 = bisect(X, c1)
# if c1 in X: i1-=1; 
# else: X.insert(i1,c1);

# i2 = bisect(X,c2)
# if c2 in X: i2-=1;
# else: X.insert(i2,c2);

# if(len(X[i2+1:])%2 != 0):
#     i2+=1
# print(X)

# if(i1%2==0):
#     X = X[0:i1+1]+X[i2:]
# else:
#     X = X[0:i1]+X[i2:]

# print(X)
#print(X[:i1]+X[i2:])
n,m,k = [int(x) for x in input().split(' ')]
K = [[] for i in range(k)]
dic = dict([])

for i in range(k):
    r,c1,c2 = [int(x) for x in input().split(' ')]
    r-=1;
    if r not in dic:
        dic.update({r:i})

    r = dic[r]
    i1 = bisect(K[r], c1)
    if c1 in K[r]: i1-=1; 
    else: K[r].insert(i1,c1);

    i2 = bisect(K[r],c2)
    if c2 in K[r]: i2-=1;
    else: K[r].insert(i2,c2);

    if(len(K[r][i2+1:])%2 != 0):
        i2+=1

    if(i1%2==0):
        K[r] = K[r][0:i1+1]+K[r][i2:]
    else:
        K[r] = K[r][0:i1]+K[r][i2:]

num = 0
for A in K:
    total = 0
    for j in range(1, len(A), 2):
        total += A[j]-A[j-1]+1
    num += total

print(n*m-num)

