a, b, c = map(int, input().split())
car = []
for _ in range(3):
    i, j = map(int, input().split())
    car.append([i, j])

car.sort()
t = [0]*101
for i,j in car:
    for k in range(i, j):
        t[k]+=1

result = 0
for i in t:
    if i==1:
        result += a
    elif i==2:
        result +=2*b
    elif i==3:
        result += 3*c

print(result)
