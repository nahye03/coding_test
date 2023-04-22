from collections import deque
f, s, g,u, d = map(int, input().split())

def bfs(f,st, end, u,d):
    visited=[0]*(f+1)
    q = deque([st])
    visited[st]=1
    while q:
        x = q.popleft()
        if x==end:
            return visited[x]-1
        if x+u<=f and not visited[x+u]:
            q.append(x+u)
            visited[x+u]=visited[x]+1
        if x-d>0 and not visited[x-d]:
            q.append(x-d)
            visited[x-d]=visited[x]+1
    return -1

result =bfs(f,s,g,u,d)
if result==-1:
    print("use the stairs")
else:
    print(result)