n = int(input())
nums = list(map(int, input().split()))

result = [-1]*n
stack=[0]
for i in range(1, n):
    while stack:
        if nums[stack[-1]]<nums[i]:
            idx =stack.pop()
            result[idx]=nums[i]
        else:
            break
    stack.append(i)

print(*result)