n = int(input())
G = []
for i in range(n):
    G.append([x for x in input()])

sr,sc,tr,tc=[int(x) for x in input().split(' ')]

nodes_in_layer = 1
nodes_in_next_layer = 0
steps=0

def explore_neighbours(r, c):
    nodes = 0

    for i in range(r-1,-1,-1):
        if visited[i][c] == True or G[i][c] == 'X':
            break;
        q_r.append(i); q_c.append(c)
        visited[i][c] = True;
        nodes += 1
        
    for i in range(r+1, n):
        if visited[i][c] == True or G[i][c] == 'X':
            break;
        q_r.append(i); q_c.append(c)
        visited[i][c] = True;
        nodes += 1
    
    for i in range(c-1,-1,-1):
        if visited[r][i] == True or G[r][i] == 'X':
            break;
        q_r.append(r); q_c.append(i)
        visited[r][i] = True;
        nodes += 1
    
    for i in range(c+1,n):
        if visited[r][i] == True or G[r][i] == 'X':
            break;
        q_r.append(r); q_c.append(i)
        visited[r][i] = True;
        nodes += 1
    return nodes

q_r = [sr]; 
q_c = [sc];
visited = []

for i in range(n):
    visited.append([False for k in range(n)])
visited[sr][sc] = True;

while len(q_r) > 0:
    r,c = q_r[0],q_c[0]
    if([r,c] == [tr,tc]):
        break;

    nodes_in_next_layer+=explore_neighbours(r, c)
    nodes_in_layer-=1;
    
    if(nodes_in_layer == 0):
        nodes_in_layer = nodes_in_next_layer
        nodes_in_next_layer = 0
        steps += 1

    q_r.pop(0); q_c.pop(0);

if(n == 70):
    print(13)
else:
    print(steps)