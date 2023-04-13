from collections import deque

n,m = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))
visited=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y, n, m):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    q.append((nx, ny))
                    visited[nx][ny]=visited[x][y]+1
bfs(0,0,n,m)
print(visited[n-1][m-1])