import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    q=deque()
    tmp=[]
    q.append((a,b))
    tmp.append((a,b))
    visited[a][b]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph) and not visited[nx][ny]:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    visited[nx][ny]=1
                    tmp.append((nx,ny))
                    q.append((nx,ny))
    return tmp

result = 0
while 1:
    visited = [[0] * n for _ in range(n)]
    flag=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                cons = bfs(i,j)
                if len(cons)>1:
                    flag=1
                    avr = sum([graph[x][y] for x,y in cons])//len(cons)
                    for x,y in cons:
                        graph[x][y]=avr
    if flag==0:
        break
    result+=1

print(result)




