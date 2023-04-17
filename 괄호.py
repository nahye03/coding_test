t = int(input())
for _ in range(t):
    s = input()
    stack =[]
    flag =0
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flag=1
                break
    if flag==0 and not stack:
        print("YES")
    else:
        print("NO")
