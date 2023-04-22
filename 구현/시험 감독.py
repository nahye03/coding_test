import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for i in a:
    if i-b<=0:
        result+=1
    else:
        result += math.ceil((i-b)/c)+1

print(result)