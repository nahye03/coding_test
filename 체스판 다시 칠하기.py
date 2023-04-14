n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input()))

result = 64
for i in range(0,n-7):
    for j in range(0,m-7):
        cnt=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0 and board[x][y]=='B':
                    cnt+=1
                elif (x+y)%2==1 and board[x][y]=='W':
                    cnt+=1
        result = min(result, cnt, 64-cnt)

print(result)