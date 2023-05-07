from collections import deque


def solution(maps):
    answer = -1
    h = len(maps)
    w = len(maps[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = 0

    while q:
        x, y, c = q.popleft()
        if x == h - 1 and y == w - 1:
            answer = c
            break
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                q.append((nx, ny, c + 1))
                maps[nx][ny] = 0

    return answer