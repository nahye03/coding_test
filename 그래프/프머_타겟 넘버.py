from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    while q:
        val, cnt = q.popleft()
        if cnt == len(numbers) and val == target:
            answer += 1
            continue
        if cnt < len(numbers):
            q.append((val + numbers[cnt], cnt + 1))
            q.append((val - numbers[cnt], cnt + 1))

    return answer

##dfs로 푸는법
answer = 0


def dfs(numbers, target, cnt, val):
    global answer
    if cnt == len(numbers) and val == target:
        answer += 1
        return
    if cnt >= len(numbers):
        return
    if cnt < len(numbers):
        dfs(numbers, target, cnt + 1, val + numbers[cnt])
        dfs(numbers, target, cnt + 1, val - numbers[cnt])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer