def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        if i==len(completion):
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer

#-------
def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        if p in dict:
            dict[p]+=1
        else:
            dict[p]=1
    for c in completion:
        dict[c]-= 1
    for key, val in dict.items():
        if val==1:
            answer = key
    return answer