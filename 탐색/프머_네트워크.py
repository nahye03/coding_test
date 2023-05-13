from collections import deque

def solution(n, computers):
    answer = 0
    v = [0] * n

    for com in range(n):
        if v[com] == 0:
            answer += 1
            q = deque()
            q.append(com)
            v[com] = 1

            while q:
                c = q.popleft()
                for i in range(n):
                    if c != n and computers[c][i] == 1 and v[i] == 0:
                        q.append(i)
                        v[i] = 1

    return answer