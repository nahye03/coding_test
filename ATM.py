n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0
sum_t = 0
for i in p:
    sum_t+=i
    result+=sum_t

print(result)