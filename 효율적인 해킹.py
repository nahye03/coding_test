import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int, input().split())
    graph[j].append(i)

def bfs(x):
    v = [0]*(n+1)
    q = deque([x])
    v[x]=1
    cnt=0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if v[i]==0:
                q.append(i)
                v[i]=1
                cnt+=1
    return cnt

mx = 0
result = []
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt>mx:
        mx = cnt
        result = [i]
    elif cnt==mx:
        result.append(i)

print(*result)