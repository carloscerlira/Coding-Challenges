def theGridSearch(G, g):
    offset = 0
    for i in range(0, R):
        if(i+r>R):
            continue;
        for j in range(0, C):
            if(j+c>C):
                continue;
            if([x[j:j+c] for x in G[i:i+r]] == g):
                return 'YES'
    return 'NO'

R,C = 3,4
r,c = 2,2 
G =[[1,2,3,3],
    [4,5,6,3],
    [7,8,9,3]]
    
g =[[6,4],
    [9,3]]
print(theGridSearch(G, g))

# cases = int(input())
# for case in range(0, cases):
#     R, C = [int(x) for x in input().split(' ')]
#     G = []
#     for i in range(0,R):
#         G.append([int(x) for x in input()])
#     r, c = [int(x) for x in input().split(' ')]
#     g = []
#     for i in range(0,r):
#         g.append([int(x) for x in input()])
#     theGridSearch(G,g)