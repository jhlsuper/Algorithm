import sys
from collections import deque

xt = [0, 1, -1, 0]
yt = [1, 0, 0, -1]
input = sys.stdin.readline
## tornado 3 -> 4 -> 0 > 1
t = int(input())
for tc in range(t):
    answer = 1e9
    tornado = []
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                tornado.append((i, j))

    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())
    # print(sx, sy, dx, dy)
    q = deque()
    q.append((sx, sy, 0))
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] =1
    while q:
        cx, cy, d = q.popleft()
        # print(cx, cy, d)
        if cx == dx and cy == dy:
            if answer > d:
                answer = d
                break
                # print(answer)
        q.append((cx, cy, d + 1))
        for i in range(4):
            nx = cx + xt[i]
            ny = cy + yt[i]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != 1 and not visited[nx][ny]:
                if maps[nx][ny] == 2:
                    if d % 3 == 2:
                        visited[nx][ny] =1
                        q.append((nx, ny, d + 1))
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny, d + 1))
    print(f"#{tc+1} {answer}")
