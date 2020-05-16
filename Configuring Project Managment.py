def BFS(adj, dic):
    def explore(node):
        for x in adj[node]:
            if visited[x] == False:
                queue.append(x)
                visited[x] = True
                not_invited.append(x)

    visited = [False for x in range(len(adj))]
    visited[0] = True; visited[1] = True;
    queue = [1]; not_invited = [1]
    k = len(adj[1])+1
    if 0 in adj[1]:
        k-=1
    while len(queue) > 0:
        if k == 0:
            break;
        k-=1
        node = queue[0]
        explore(node)
        queue.pop(0) 

    invited = []
    for x in adj[0]:
        if x not in not_invited:
            invited.append(x)

    if len(invited) == 0:
        print(-1)
        return 

    invited = [dic[x] for x in invited]
    invited.sort()
    for x in invited:
        print('{} '.format(x), end='')

t = int(input())

for j in range(t):
    n,m = [int(x) for x in input().rstrip().split()]
    adj = [set for x in range(n)]
    dic1 = {1:0,2:1}
    dic2 = {0:1,1:2}
    counter = 2
    for i in range(m):
        p1,p2=[int(x) for x in input().rstrip().split()]
        if(p1 not in dic1):
            dic1.update({p1:counter})
            dic2.update({counter:p1})
            counter +=1 
        if(p2 not in dic1):
            dic1.update({p2:counter})
            dic2.update({counter:p2})
            counter +=1
        p1,p2 = dic1[p1], dic1[p2] 
        if p2 not in adj[p1]: adj[p1].append(p2)
        if p1 not in adj[p2]: adj[p2].append(p1)
    BFS(adj, dic2)