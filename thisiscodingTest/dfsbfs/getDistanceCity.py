from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [0] * (N + 1)
# print(graph)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)

    if (len(answer)) == 0:
        print(-1)
        return
    else:
        answer.sort()
        for i in answer:
            print(i)


bfs(X)
