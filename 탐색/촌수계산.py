from collections import deque

n = int(input())
a,b = map(int, input().split())
m = int(input())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(st,end,graph):
    visited = [0]*(n+1)
    q = deque([st])
    visited[st]=1
    while q:
        x = q.popleft()
        if x==end:
            return visited[x]-1
        for g in graph[x]:
            if not visited[g]:
                q.append(g)
                visited[g]=visited[x]+1
    return -1

print(bfs(a,b,graph))