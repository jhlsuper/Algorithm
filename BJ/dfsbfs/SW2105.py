## dfs 나 bfs를 이용해서 풀어보자 bfs가 큐
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, -1, 1, 1]  # 11시 1시 5시 7시
dy = [-1, 1, 1, -1]
T = int(input())
for t in range(T):
    answer = 0
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(i, j)
            times = 0
            visited = [[0] * N for _ in range(N)]
            # print(visited)
            q = deque()
            q.append((i, j, 0, [maps[i][j]]))
            # x, y, c, f = i, j, 0, [maps[i][j]]

            while q:
                x, y, c, f = q.popleft()
                print(x, y, c, f)
                # if x == i and y == j:
                #     if c > answer:
                #         answer = c
                #     break


                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # print(nx, ny, "hi")
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and maps[nx][ny] not in f:
                        visited[x][y] = 1
                        if nx == i and ny == j:
                            print(c, "hihihihihihi")
                            if c > answer:
                                answer = c

                                break
                        f.append(maps[nx][ny])
                        q.append((nx, ny, c + 1, f))
    print(answer)
