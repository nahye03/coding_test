import sys
sys.setrecursionlimit(10000)

def dfs(graph, x,y):
    dx =[-1,1,0,0]
    dy =[0,0,-1,1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(graph, nx, ny)

t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        i,j = map(int, input().split())
        graph[i][j] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                dfs(graph, i, j)
                cnt+=1
    print(cnt)



