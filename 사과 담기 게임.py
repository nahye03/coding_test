n,m = map(int, input().split())
j = int(input())

nx = [1,m]
result = 0
for _ in range(j):
    ap = int(input())
    if ap<nx[0]:
        result+=(nx[0]-ap)
        nx=[ap,ap+m-1]
    elif ap>nx[1]:
        result+=(ap-nx[1])
        nx = [ap-m+1,ap]

print(result)
