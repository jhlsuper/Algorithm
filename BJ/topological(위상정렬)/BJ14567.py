import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [1] * (N + 1)

arr = []

for i in range(M):
    a, b, = map(int, input().split())
    arr.append((a, b))
arr.sort()
for a, b in arr:
    if graph[b] <= graph[a]:
        graph[b] = graph[a] + 1
    # print(graph)
print(*graph[1:])
