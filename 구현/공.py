m = int(input())

cup={}
for i in range(1,4):
    cup[i]=i
for _ in range(m):
    x, y = map(int, input().split())
    tmp = cup[x]
    cup[x] = cup[y]
    cup[y]=tmp

print(*[k for k,v in cup.items() if v==1])