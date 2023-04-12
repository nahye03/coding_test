n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

nums=[]
for line in lines:
    num=''
    for l in line:
        if l.isdigit():
            num+=l
        else:
            if num:
                nums.append(int(num))
                num=''
    if num:
        nums.append(int(num))
        num = ''
nums.sort()
for i in nums:
    print(i)

