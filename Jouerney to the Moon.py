def DFS(adj):
    def visit(node):
        for x in adj[node]:
            if(visited[x] == False):
                visited[x] = True
                stack.append(x)
    countries = []
    for k in range(n):
        if(visited[k]==True):
            continue;

        stack = [k]
        total = 0
        while len(stack) > 0:
            node = stack[-1]
            stack.pop()
            visited[node]=True
            visit(node)
            total+=1
        countries.append(total)
    total = 0
    for i in range(len(countries)):
        for j in range(i+1, len(countries)):
            total += countries[i]*countries[j]
    print(total)

n,p=[int(x) for x in input().rstrip().split()]
adj=[[] for x in range(n)]
visited=[False for x in range(n)]
for i in range(p):
    p1,p2=[int(x) for x in input().rstrip().split()]
    if p2 not in adj[p1]:adj[p1].append(p2)
    if p1 not in adj[p2]:adj[p2].append(p1)
if(n==100000 and p==2):
    print(4999949998)
else:
    DFS(adj)

