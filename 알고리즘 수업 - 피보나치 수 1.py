n = int(input())

def fibo(n):
    f=[0]*(n+1)
    f[1]=1
    f[2]=1
    for i in range(3, n+1):
        f[i]=f[i-2]+f[i-1]
    return f[n]

print(fibo(n), n-2)