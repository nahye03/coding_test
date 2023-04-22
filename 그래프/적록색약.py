from collections import deque

n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
v_no = [[0]*n for _ in range(n)]
v_yes = [[0]*n for _ in range(n)]
def bfs(x,y,graph, visited, flag):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    if flag:
        if graph[x][y]=='B':
            color = ['B']
        else:
            color = ['R', 'G']
    else:
        color=[graph[x][y]]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if graph[nx][ny] in color and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=1

result = [0,0]
for x in range(n):
    for y in range(n):
        if not v_no[x][y]:
            bfs(x,y,graph,v_no,False)
            result[0]+=1
        if not v_yes[x][y]:
            bfs(x,y,graph,v_yes,True)
            result[1] += 1
print(*result)


