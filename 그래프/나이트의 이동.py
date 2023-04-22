from collections import deque

move = [(-2, 1),(-2,-1),(2,1),(2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]

def bfs(st,end,l):
    visited = [[0]*l for _ in range(l)]
    q = deque()
    q.append(st)
    visited[st[0]][st[1]]=1
    while q:
        x, y = q.popleft()
        if x==end[0] and y==end[1]:
            print(visited[x][y]-1)
            break
        for i in range(8):
            nx = x+move[i][0]
            ny = y+move[i][1]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1


t = int(input())
for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    bfs(start, end, l)

