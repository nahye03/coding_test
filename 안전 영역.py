import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph =[]
mh=1
for _ in range(n):
    arr=list(map(int, input().split()))
    graph.append(arr)
    mh=max(mh, max(arr))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,v,h):
    q=deque()
    q.append((x,y))
    v[x][y]=1

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>h and v[nx][ny]==0:
                    q.append((nx,ny))
                    v[nx][ny]=1

result = 1
for h in range(1, mh):
    v = [[0] * n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and v[i][j]==0:
                bfs(i,j,v,h)
                cnt+=1
    result = max(result, cnt)

print(result)
