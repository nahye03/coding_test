pw = []
inp = input()
while inp!='end':
    pw.append(inp)
    inp = input()

result = [False]*len(pw)
moum= ['a','e','i','o','u']
for i in range(len(pw)):
    cnt =1
    past_mj = 1 if pw[i][0] in moum else 0
    if past_mj : result[i]=True
    for j in range(1, len(pw[i])):
        #모음 자음 판단하여 개수 카운팅
        now_mj = 1 if pw[i][j] in moum else 0
        if past_mj == now_mj:
            cnt+=1
            if cnt==3:
                result[i]=False
                break
        else:
            past_mj = now_mj
            cnt=1

        # 같은 글자
        if pw[i][j]==pw[i][j-1] and pw[i][j]!='e' and pw[i][j]!='o':
            result[i]=False
            break

        if pw[i][j] in moum:
            result[i]=True

for i in range(len(pw)):
    if result[i]:
        print(f'<{pw[i]}> is acceptable.')
    else:
        print(f'<{pw[i]}> is not acceptable.')

