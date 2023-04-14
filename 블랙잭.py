n,m = map(int,input().split())
nums = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp<=m:
                    result = max(result, tmp)

print(result)



