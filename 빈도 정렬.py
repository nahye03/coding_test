N,C = map(int, input().split())
mes = list(map(int, input().split()))

def sol(n, c, mes):
    order = {}
    for i in mes:
        if i not in order:
            order[i] = 0
        order[i]+=1

    result = sorted(order.items(), key=lambda x:x[1], reverse=True)
    for k,v in result:
        for i in range(v):
            print(k, end=' ')

sol(N,C,mes)