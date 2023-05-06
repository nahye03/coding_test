def solution(citations):
    answer = 0
    for i in range(len(citations) + 1, -1, -1):
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
        if i <= cnt:
            answer = i
            break

    return answer