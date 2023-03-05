import sys
from _collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(arr, visited, time):
    q = deque()
    q.append((0, 0))
    while q:
        temp = q.pop()
        # print(temp)
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:
                    continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    q.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        q.append((nx, ny))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))
    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    s = [0, 0]
    g = [N - 1, N - 1]

    bfs(arr, visited, time)
    print(f'#{t} {time[N - 1][N - 1]}')
