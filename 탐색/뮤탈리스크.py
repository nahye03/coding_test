from collections import deque
from itertools import permutations

n = int(input())
pow = list(map(int, input().split()))+[0]*(3-n)

attack =list(permutations([9,3,1]))
mp = max(pow)+1
dp = [[[0]*mp for _ in range(mp)] for _ in range(mp)]

q = deque()
q.append(pow)
dp[pow[0]][pow[1]][pow[2]]=1

while q:
    x,y,z = q.popleft()
    if x==0 and y==0 and z==0:
        print(dp[x][y][z]-1)
        break
    for a1,a2,a3 in attack:
        x_ = x-a1 if x-a1>0 else 0
        y_ = y - a2 if y - a2 > 0 else 0
        z_ = z - a3 if z - a3 > 0 else 0
        if dp[x_][y_][z_]==0:
            dp[x_][y_][z_] = dp[x][y][z]+1
            q.append([x_,y_,z_])


