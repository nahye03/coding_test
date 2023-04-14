k=int(input())
order = list(map(int, input().split()))
l = len(order)
result = [[] for _ in range(k)]

def sol(st, end, level):
    if st==end:
        result[level].append(order[st])
        return
    mid = (st+end)//2
    result[level].append(order[mid])
    sol(st,mid-1,level+1)
    sol(mid+1, end, level+1)

sol(0,l-1,0)
for i in result:
    print(*i)