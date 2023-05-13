import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))

start, dest = map(int, input().split())
cost = [int(1e9)]*(n+1)

def dijkstra(st):
    h=[]
    heapq.heappush(h,(0,st))
    cost[st] = 0

    while h:
        c_now, now = heapq.heappop(h)

        if cost[now]<c_now:
            continue

        for i in graph[now]:
            c_next = c_now+i[1]
            if c_next<cost[i[0]]:
                heapq.heappush(h,(c_next, i[0]))
                cost[i[0]] = c_next

dijkstra(start)
print(cost[dest])