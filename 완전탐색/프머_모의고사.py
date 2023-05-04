def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]
    result = []

    for idx, val in enumerate(answers):
        if p1[idx % len(p1)] == val:
            cnt[0] += 1
        if p2[idx % len(p2)] == val:
            cnt[1] += 1
        if p3[idx % len(p3)] == val:
            cnt[2] += 1

    for idx, val in enumerate(cnt):
        if val == max(cnt):
            result.append(idx + 1)

    return result

