import sys
input =sys.stdin.readline

s = input().rstrip()
q = int(input())

prex=[[0]*26]

prex[0][ord(s[0])-ord('a')]=1
for i in range(1, len(s)):
    prex.append(prex[-1][:])
    idx = ord(s[i])-ord('a')
    prex[i][idx]+=1

for _ in range(q):
    a, l, r = input().split()
    if l=='0':
        print(prex[int(r)][ord(a) - ord('a')])
    else:
        print(prex[int(r)][ord(a)-ord('a')]-prex[int(l)-1][ord(a)-ord('a')])
