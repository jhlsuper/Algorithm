import sys
from collections import deque

# 2차원 배열을 사용하면 메모리 초과가 난다. 따라서 인접리스트를 사용해야된다.
input = sys.stdin.readline
INF = 1e9
V, E = map(int, input().split())
K = int(input())  ##시작 좌표
graph = []
d = [INF for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]

for _ in range(V + 1):
    graph.append([])

for i in range(V):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    # graph[a][b] = w
print(graph)
d[K] = 0
min = INF
current = -1
dq = deque()
# for i in range(V):
#     current = -1
#     min = INF
#     for j in range(V):
#         if (not visited[j] and min > d[j]):
#             min = d[j]
#             current = j
#     if current == -1 or current == V:
#         break
#     visited[current] = True
#     for j in range(V):
#         if not visited[j] and graph[current][j] != 0 and d[j] > min + graph[current][j]:
#             d[j] = min + graph[current][j]
dq.append([K, 0])
while dq:
    temp = deque.popleft()
    cur = temp[0]
    if visited[cur]:
        continue
    visited[cur] = True
    for j in graph[cur]:
        if d[j[0]] >d[cur] + j[1]:
            d[j[0]] = d[cur]+j[1]
            dq.append([j[0],d[j[0]]])
print(d)
for i in range(1, V + 1):
    if d[i] != INF:
        print(d[i])
    else:
        print("INF")
