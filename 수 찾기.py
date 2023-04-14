n = int(input())
a=list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

a.sort()
for num in target:
    l,r = 0, n-1
    result = False

    while l<=r:
        mid = (l+r)//2
        if num==a[mid]:
            result = True
            break
        elif num>a[mid]:
            l=mid+1
        else:
            r = mid-1
    print(1) if result else print(0)
