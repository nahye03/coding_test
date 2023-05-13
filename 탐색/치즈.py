from collections import deque

n,m = map(int, input().split())
graph = []
cnt=0
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    cnt+=sum(arr)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0]=1
    melt = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                visited[nx][ny] = 1
                if graph[nx][ny]==1:
                    melt.append((nx,ny))
                else:
                    q.append((nx,ny))

    for x,y in melt:
        graph[x][y] = 0

    return len(melt)

time =1
while True:
    visited=[[0]*m for _ in range(n)]
    melt_cnt = bfs()
    cnt-=melt_cnt
    if cnt==0:
        print(time, melt_cnt, sep='\n')
        break
    else:
        time+=1


