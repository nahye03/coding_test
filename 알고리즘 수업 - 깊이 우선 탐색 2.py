import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited = [0]*(len(graph))
    cnt=0
    stack=[x]
    while stack:
        node = stack.pop()
        if not visited[node]:
            cnt+=1
            visited[node]=cnt
            stack.extend(sorted(graph[node]))
    return visited

result = dfs(r)
for i in range(1, n+1):
    print(result[i])