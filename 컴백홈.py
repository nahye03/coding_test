r,c,k = map(int, input().split())
graph=[]
for _ in range(r):
    graph.append(list(input()))

visited=[[0]*c for _ in range(r)]
visited[r-1][0]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0
tmp=[(r-1,0)]
route=[]

def dfs(x,y,cnt,tmp):
    global result
    if cnt==k and x==0 and y==c-1:
        result+=1
        route.append(tmp[:])
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
            if visited[nx][ny]==0 and graph[nx][ny]!='T':
                visited[nx][ny]=1
                tmp.append((nx,ny))
                dfs(nx,ny,cnt+1,tmp)
                visited[nx][ny]=0
                tmp.pop()
dfs(r-1,0,1,tmp)
print(result)
print(route)