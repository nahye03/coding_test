price =[1, 2, 3, 2, 3]

def sol(price):
    answer=[0]*len(price)
    stk = [(0,price[0])]
    for i in range(1, len(price)):
        while stk:
            if stk[-1][1]>price[i]:
                idx = stk.pop()[0]
                answer[idx]=i-idx
            else:
                break
        stk.append((i,price[i]))
    while stk:
        idx = stk.pop()[0]
        answer[idx]=len(price)-idx-1

    return answer

result = sol(price)
print(result)