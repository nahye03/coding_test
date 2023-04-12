x = int(input())
cnt =1
while x>cnt:
    x-=cnt
    cnt+=1

if cnt%2==0:
    print(str(x)+'/'+str(cnt-x+1))
else:
    print(str(cnt-x+1)+'/'+str(x))