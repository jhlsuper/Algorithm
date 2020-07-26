from collections import deque

N, M, V = map(int, input().split())

graph = [[] for i in range(0, 1001)]

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in graph:
    i.sort()

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for adjacent in graph[v]:
        if visited[adjacent] == False:
            dfs(adjacent)

def bfs(v):
    willVisit = deque()
    visited[v] = True
    willVisit.append(v)
    print(v, end=" ")
    while willVisit:
        nowVisit = willVisit.popleft()
        for adjacent in graph[nowVisit]:
            if visited[adjacent] == False:
                print(adjacent, end=" ")
                visited[adjacent] = True
                willVisit.append(adjacent)

visited = [False for i in range(0, 1001)]

dfs(V)

visited = [False for i in range(0, 1001)]
print()
bfs(V)