import sys
input = sys.stdin.readline
from collections import deque

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(x):
    v = [0] * (len(graph))
    q = deque([x])
    cnt=1
    v[x]=cnt
    while q:
        x = q.popleft()
        for i in sorted(graph[x]):
            if not v[i]:
                q.append(i)
                cnt+=1
                v[i]=cnt
    return v

result = bfs(r)
for i in range(1, n+1):
    print(result[i])