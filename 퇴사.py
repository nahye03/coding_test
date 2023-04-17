n = int(input())
t=[0]*(n+1)
p=[0]*(n+1)
for i in range(n):
    a,b =map(int, input().split())
    t[i]=a
    p[i]=b

dp = [0]*(n+1)
dp[n] = p[n] if t[n]<=1 else 0
for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])