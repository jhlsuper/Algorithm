from collections import deque

global answer
answer = 0
q = deque()
M, N = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
maps = [list(map(int, input().split())) for _ in range(N)]
print(maps)
z = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            q.append((i, j))


def bfs():
    while q:
        x, y = q.popleft()
        # print(x, y, z)
        # if z > answer:
        #     answer = z
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny, maps[nx][ny])
            if 0 <= nx < N and 0 <= ny < M:

                if maps[nx][ny] == 0 and maps[nx][ny] != -1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    # maps[nx][ny] = 1
                    # print(nx, ny, z)


res = 0
bfs()
for i in maps:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
