import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
cnt=0
def dfs(x):
    global cnt
    cnt+=1
    visited[x]=cnt
    for i in sorted(graph[x]):
        if not visited[i]:
            dfs(i)

dfs(r)
for i in range(1, n+1):
    print(visited[i])

