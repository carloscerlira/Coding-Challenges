def roadsAndLibraries(adj, cr, cl):
    def visit(node):
        for x in adj[node]:
            if(visited[x] == False):
                visited[x] = True
                stack.append(x)
    
    total = 0
    visited = [False for x in range(len(adj))]
    
    for k in range(len(adj)):
        if(len(adj[k])==0):
            total += cl;
            continue;

        if(visited[k]==True):
            continue;
        stack = [k]
        dt = 0
        while len(stack) > 0:
            node = stack[-1]
            stack.pop()
            visited[node]=True
            visit(node)
            dt+=1
        total += (dt-1)*cr+cl
    print(total)

q=int(input())
for i in range(q):
    n,m,cl,cr=[int(x) for x in input().split()]
    adj=[[] for x in range(n)]
    for i in range(m):
        c1,c2=[int(x) for x in input().split()]
        c1,c2=c1-1,c2-1;
        if c2 not in adj[c1]: adj[c1].append(c2)
        if c1 not in adj[c2]: adj[c2].append(c1)
    if cl < cr:
        print(n*cl)
        continue;
    #print(ad   j)
    roadsAndLibraries(adj, cr, cl)


# 1
# 8 6 5 2
# 7 1
# 1 3
# 3 2
# 2 1
# 5 6
# 6 8

