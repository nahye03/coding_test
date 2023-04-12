
nums=[]
while 1:
    try:
        n = int(input())
        nums.append(n)
    except:
        break

for num in nums:
    n1 = '1'
    while int(n1)%num!=0:
        n1+='1'
    print(len(n1))