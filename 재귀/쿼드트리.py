import sys
sys.setrecursionlimit(10**6)

n = int(input())
img = []
for _ in range(n):
    img.append(list(map(int, input())))

def sol(x,y,n):
    color = img[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=img[i][j]:
                print('(',end='')
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2, y, n // 2)
                sol(x+n//2, y+n//2, n // 2)
                print(')',end='')
                return
    print(color,end='')

sol(0,0,n)