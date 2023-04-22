n = int(input())

members =[]
for i in range(n):
    age, name = input().split()
    members.append((i,int(age), name))

members.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    print(members[i][1], members[i][2])