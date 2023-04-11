n = int(input())
names = []
for _ in range(n):
    names.append(input())

names.sort()

result =[]
cnt =1
now_n = names[0][0]

for i in range(1, n):
    if now_n == names[i][0]:
        cnt+=1
        if cnt == 5:
            result.append(now_n)
    else:
        cnt=1
        now_n = names[i][0]

if result:
    print(''.join(i for i in result))
else:
    print('PREDAJA')