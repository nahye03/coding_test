import math


def solution(progresses, speeds):
    answer = []
    idx = 0
    release = []

    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        release.append(days)
        if release[idx] < days:
            answer.append(i - idx)
            idx = i

    answer.append(len(progresses) - idx)

    return answer