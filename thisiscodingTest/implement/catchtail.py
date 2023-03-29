n, m, k = map(int, input().split())
global visited
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

# temp.append((x, y))

def dfs(x, y, temp, visited):
    # print(x, y, visited)

    visited[x][y] = True
    temp.append((x, y))
    print(temp)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < y and not visited[nx][ny] and maps[nx][ny] != 0:
            # if maps[nx][ny] == 2:
            temp.append((nx, ny))
            print(nx, ny)
            dfs(nx, ny, temp, visited)


# print(startline[0][0], startline[0][1])


def findlines():
    for i in range(m):
        temp = []
        visited = [[False] * n for _ in range(n)]
        dfs(startline[i][0], startline[i][1], temp, visited)

        lines[i] = (temp)


findlines()
print(lines)
