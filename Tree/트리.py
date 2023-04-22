n =int(input())
arr = list(map(int, input().split()))
target =int(input())

tree=[[] for _ in range(n)]
for i in range(n):
    if arr[i]==-1:
        root = i
    elif i!=target:
        tree[arr[i]].append(i)

cnt=0
if target!=root:
    stack=[root]
    while stack:
        x = stack.pop()
        if not tree[x]:
            cnt+=1
        for i in tree[x]:
            stack.append(i)

print(cnt)