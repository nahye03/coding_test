from collections import deque


def solution(begin, target, words):
    answer = 0

    q = deque()
    q.append((begin, 0))

    while q:
        temp, c = q.popleft()
        if temp == target:
            answer = c
            break
        for word in words:
            cnt = 0
            for i in range(len(temp)):
                if temp[i] == word[i]:
                    cnt += 1
            if cnt == len(temp) - 1:
                q.append((word, c + 1))
                words.remove(word)

    return answer