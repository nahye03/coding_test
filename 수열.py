import sys
input =sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

prex = [0]
for i in range(n):
    prex.append(prex[i]+nums[i])

mx = prex[k-1]
for i in range(1, n-k+1):
    tmp = prex[i+k-1]-prex[i-1]
    if tmp>mx:
        mx=tmp

print(mx)

##다른 방법
pref =[sum(nums[:k])]
for i in range(n-k):
    pref.append(pref[i]+nums[i+k]-nums[i])
print(max(pref))