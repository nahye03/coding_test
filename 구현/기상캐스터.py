h,w = map(int, input().split())
sky = []
for _ in range(h):
    sky.append(list(input()))

result = [[-1]*w for _ in range(h)]

for i in range(h):
    cloud_idx = -1
    for j in range(w):
        if sky[i][j]=='c':
            result[i][j] = 0
            cloud_idx = j
        else:
            if cloud_idx!=-1:
                result[i][j] = j-cloud_idx

for i in range(h):
    print(*result[i])