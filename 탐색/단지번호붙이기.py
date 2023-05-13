n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return 0
    else:
        if graph[x][y]==0:
            return 0
        else:
            graph[x][y]=0
            return dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)+1

result =[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(dfs(i,j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])


#--------------------bfs
from collections import deque

n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy =[0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    graph[x][y]=0
    cnt =0
    while q:
        a, b = q.popleft()
        cnt+=1
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1:
                    q.append([nx,ny])
                    graph[nx][ny]=0
    return cnt

result =[]
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            result.append(bfs(x, y))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])


#----------dfs 다른 방법
n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy =[0,0,-1,1]
cnt=0

def dfs(x, y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return False
    else:
        if graph[x][y]==1:
            graph[x][y]=0
            cnt+=1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                dfs(nx,ny)
            return True
        return False

result = []
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            result.append(cnt)
            cnt=0
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])