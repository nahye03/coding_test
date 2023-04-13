import sys
input =sys.stdin.readline
from collections import deque

h,w = map(int, input().split())
graph=[]
for _ in range(h):
    graph.append(list(input().rstrip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph, a, b):
    q = deque()
    q.append((a,b))
    v = [[0] * w for _ in range(h)]
    v[a][b]=1
    mxd = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]):
                continue
            elif graph[nx][ny]=='L' and v[nx][ny]==0:
                q.append((nx,ny))
                v[nx][ny]=v[x][y]+1
                mxd = max(mxd, v[nx][ny])
    return mxd

result=0
for i in range(h):
    for j in range(w):
        if graph[i][j]=='L':
            result = max(result, bfs(graph, i, j))

print(result-1)
