import sys
input =sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))

pref=[0]
for i in range(n):
    pref.append(num[i]+pref[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(pref[j]-pref[i-1])