import sys
from collections import deque
input =sys.stdin.readline

m,n,k = map(int, input().split())

graph = [[0]*n for _ in range(m)]
for _ in range(k):
    y1,x1,y2,x2 = map(int, input().split())
    for i in range(x1,x2):
        graph[i][y1:y2]=[1]*(y2-y1)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y]=1
    cnt=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny]=1
                    cnt+=1
    return cnt

result =[]
for a in range(m):
    for b in range(n):
        if graph[a][b]==0:
            result.append(bfs(a,b))
print(len(result))
result.sort()
print(*result)
