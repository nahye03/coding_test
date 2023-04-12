import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,d = map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited=[[0]*m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

x,y=r,c
visited[x][y]=1
cnt =1

while 1:
    check=False
    for _ in range(4):
        nd = (d+3)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        d=nd
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                x, y= nx, ny
                visited[x][y] = 1
                cnt += 1
                check = True
                break
    if not check:
        x = x-dx[d]
        y = y-dy[d]
        if 0<=x<n and 0<=y<m and graph[x][y]==1:
            break


print(cnt)