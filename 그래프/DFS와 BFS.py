from collections import deque

n,m,v = map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

v_d = [0] * (n+1)
v_b = [0] * (n+1)

def dfs(v_d, graph, v):
    v_d[v]=1
    print(v, end=' ')
    for i in graph[v]:
        if not v_d[i]:
            dfs(v_d, graph, i)

def bfs(v_b, graph, v):
    q = deque([v])
    v_b[v]=1
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not v_b[i]:
                q.append(i)
                v_b[i]=1


dfs(v_d, graph, v)
print()
bfs(v_b, graph, v)