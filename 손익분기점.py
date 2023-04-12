a,b,c = map(int, input().split())

result = 0
if c>b:
    result = (a // (c - b)) + 1
else:
    result = -1

print(result)