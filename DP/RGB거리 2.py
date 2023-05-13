n = int(input())
home = []
for _ in range(n):
    home.append(list(map(int, input().split())))

result = []
for i in range(3):
    dp=[[0,0,0] for _ in range(n)]
    dp[0][i] = home[0][i]
    dp[0][i-1] = 1001
    dp[0][i-2] = 1001

    for h in range(1, n):
        dp[h][0] = home[h][0] + min(dp[h-1][1], dp[h-1][2])
        dp[h][1] = home[h][1] + min(dp[h - 1][0], dp[h - 1][2])
        dp[h][2] = home[h][2] + min(dp[h - 1][0], dp[h - 1][1])

    result.append(min(dp[n-1][i-1], dp[n-1][i-2]))

print(min(result))