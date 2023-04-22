from collections import deque

n = int(input())
m = int(input())

graph =[[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(x):
    q = deque([x])
    v = [0]*(n+1)
    v[x] =1
    cnt = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not v[i]:
                q.append(i)
                v[i]=1
                cnt+=1
    return cnt

print(bfs(1))