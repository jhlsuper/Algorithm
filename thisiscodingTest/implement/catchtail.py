from collections import deque

n, m, k = map(int, input().split())

maps = [[] for _ in range(n)]  ##지도 정보
lines = [[] for _ in range(m)]  ##사람 줄 정보
startline = []  ## 라인 시작좌표 저장 하는 곳
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        maps[i].append(temp[j])
        if temp[j] == 1:
            startline.append((i, j))
print(maps)


# def findLine(x, y, i):  ##x,y i는 몇번째
# temp = []

## 그냥 시뮬로 계속 찾기

def findLine(x, y):
    line = []
    index = 1
    while True:
        if index == 1:

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 2:
                    line.append((nx, ny))
                    index += 2
                    print(nx, ny)
        if index == 2:
            flag = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 2:
                    line.append((nx, ny))
                    print(nx, ny)
                    flag = True
            if not flag:
                index = 3
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 3:
                        line.append((nx, ny))
                        print(nx, ny)
        if index == 3:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 4:
                    line.append((nx, ny))
                    print(nx, ny)
                if maps[nx][ny] == 1:
                    break
    return line


def findlines():
    for i in range(m):
        visited = [[False] * n for _ in range(n)]

        # dfs(startline[i][0], startline[i][1], visited, line)
        print(findLine(startline[i][0], startline[i][1]))
        # line = bfs(startline[i][0], startline[i][1], visited)

        # lines[i] = line


findlines()
# print(lines)
