while 1:
    s = input()
    if s=='.':
        break
    stk =[]
    flag =True
    for i in s:
        if i=='(' or i=='[':
            stk.append(i)
        elif i==')':
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop()
            else:
                flag=False
                break
        elif i==']':
            if len(stk)!=0 and stk[-1]=='[':
                stk.pop()
            else:
                flag = False
                break
    if len(stk)!=0:
        flag = False
    print('yes') if flag else print('no')