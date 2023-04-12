n = int(input())

record=[]
for _ in range(n):
    team, t = input().split()
    team = int(team)
    ss = int(t.split(':')[0])*60 + int(t.split(':')[1])
    record.append((team, ss))

result = [0,0]
score = [0,0]
prev_team = record[0][0]
prev_time = record[0][1]
score[prev_team-1]+=1
for i in range(1, n):
    now_team = record[i][0]
    now_time = record[i][1]
    score[now_team-1]+=1

    if prev_time==-1:
        prev_team = now_team
        prev_time = now_time
    else:
        result[prev_team - 1] += now_time - prev_time
        if score[0]==score[1]:
            prev_team = now_team
            prev_time = -1
        else:
            prev_team = score.index(max(score)) + 1
            prev_time = now_time

if score[0]!=score[1]:
    result[prev_team-1]+= (48*60)-prev_time

for r in result:
    mm = r//60
    ss = r%60
    print(f'{mm:02}:{ss:02}')







