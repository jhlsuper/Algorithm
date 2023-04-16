## 1.동일한 숫자가 인접해 있을때 동일한 그룹

## 모든 그룹쌍의 조화로움의 합
## 2.A,B 그룹의 조화로움 (a의 칸수의 + b의 칸의수) * a의 숫자값, b의 숫자값 * 맞다아있는 변의수

##맞 닿아 있는 그림끼리만 

##3. 그림 회전 
## 십자 부분과 : 반시계 90도 통짜로 움직임 
## 십자 아닌부분  각각 개별적으로 시계 방향 90도 회전

##다시 점수 구하기
import sys
from collections import deque
from itertools import combinations

global visited
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
input = sys.stdin.readline
groups = []  ##그룹들 값 넣어주는 배열
groupsIndex = []  ## 그룹이 어떤 숫자로 이루어져있는지 넣어주는 배열

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
half = n // 2


def pRotate():
    for i in range(n):
        for j in range(n):
            if i == half:
                arr[i][j] = maps[j][i]
            if j == half:
                arr[i][j] = maps[n - j - 1][n - i - 1]


def sRotate(x, y, l):
    for i in range(x, x + l):
        for j in range(y, y + l):
            nx, ny = i - x, j - y
            rx, ry = ny, l - nx - 1
            arr[rx + x][ry + y] = maps[i][j]


def findGroups():
    # groups = []
    global visited
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(findGroupsdfs(i, j))

    for i in range(len(groups)):
        x = groups[i][0][0]
        y = groups[i][0][1]
        groupsIndex.append(maps[x][y])


def findGroupsdfs(x, y):
    eachTeam = []
    # tempgroup.append((x, y))
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()  # this x this y
        eachTeam.append((tx, ty))
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[tx][ty] == maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return eachTeam


def getScore():
    index = []
    score = 0
    for i in range(len(groups)):
        index.append(i)

    for i in combinations(index, 2):  ##순열로 확인
        ##배열 2개중 하나를 (길이가 짧은걸 골라서 )
        ## 모든 원소에 대해서 4방탐색 - 점수 구하기
        fiIndex = i[0]
        secIndex = i[1]
        fiLen, secLen = len(groups[fiIndex]), len(groups[secIndex])
        if fiLen <= secLen:
            sGroup = groups[fiIndex]  ##배열의 길이가 짧은 배열
            cGroup = groups[secIndex]  ## 몇개의 면이 인접한지 보는 배열
        else:
            sGroup = groups[secIndex]  ##start Group
            cGroup = groups[fiIndex]  ## compare Group

        count = 0  ## 인접한 면의 갯수

        for x, y in sGroup:
            ## 4방 탐색하여 cGroup에 좌표가 있다면 1씩 추가 !
            for r in range(4):
                nx = x + dx[r]
                ny = y + dy[r]
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) in cGroup:
                        count += 1
        # print(sGroup, cGroup, count)
        score += (fiLen + secLen) * groupsIndex[fiIndex] * groupsIndex[secIndex] * count
    return score


findGroups()
# print(groups, groupsIndex)
print(getScore())
print(maps)
answer += getScore()
for t in range(3):
    arr = [[0] * n for _ in range(n)]
    pRotate()
    # print(arr)
    sRotate(0, 0, half)
    sRotate(0, half + 1, half)
    sRotate(half + 1, 0, half)
    sRotate(half + 1, half + 1, half)

    for i in range(n):
        for j in range(n):
            maps[i][j] = arr[i][j]
    # print(maps)
    groups = []
    findGroups()
    # print(groups)
    # print(getScore())
    answer += getScore()
print(answer)
