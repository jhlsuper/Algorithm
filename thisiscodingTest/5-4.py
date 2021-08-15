## 미로탈출 문제 책 pg 152 ##

##사용자 위치 1,1 출구 n,m  괴물있는곳 0 없는곳 1 최소 칸의 개수
## 시작칸과 마지막 칸 모두 포함

## 입력 예시
## 5 6
## 101010
## 111111
## 000001
## 111111
## 111111
## BFS로 푸는 문제

##BFS는 시작 지점에서 가까운 노드부터 차례대로 참색하기 때문에

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
## 이동할 네 방향  상/하/좌/우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ## 공간을 벗어난경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            ## 벽인경우
            if graph[nx][ny] == 0:
                continue
            ## 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
