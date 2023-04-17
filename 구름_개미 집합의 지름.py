from collections import deque

n,d = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
q=deque()
q.append(p[0])
result=1
for i in range(1,n):
    while q:
        if p[i]-q[0]<=d:
            break
        else:
            q.popleft()
    q.append(p[i])
    result = max(result, len(q))

print(len(p)-result)


