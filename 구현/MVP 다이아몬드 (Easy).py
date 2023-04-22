import sys
input = sys.stdin.readline

n = int(input())
s,g,p,d = map(int, input().split())
mvp = list(input().strip())

result = 0
prev =0
for i in mvp:
    if i=='B':
        prev = s - 1 - prev
        result+= prev
    elif i=='S':
        prev = g - 1 - prev
        result+=prev
    elif i=='G':
        prev = p - 1 - prev
        result+=prev
    elif i=='P':
        prev = d - 1 - prev
        result+=prev
    elif i=='D':
        prev = d
        result+=prev

print(result)
