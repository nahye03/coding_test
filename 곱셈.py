A, B, C = map(int, input().split())

def sol(a, b):
    if b==1:
        return a%C
    else:
        tmp = sol(a, b//2)
        if b%2==0:
            return tmp*tmp%C
        else:
            return tmp*tmp*a%C

print(sol(A,B))