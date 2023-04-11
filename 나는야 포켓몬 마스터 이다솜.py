import sys
input = sys.stdin.readline

n,m = map(int, input().split())
names={}
for i in range(1, n+1):
    a=input().strip()
    names[i]=a
    names[a] = i

for _ in range(m):
    p = input().rstrip()
    if p.isalpha():
        print(names[p])
    else:
        print(names[int(p)])
