import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

print(round(sum(nums)/n))

nums.sort()
print(nums[n//2])

dic = dict()
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
mx = max(dic.values())
mx_dic=[]
for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(nums)-min(nums))
