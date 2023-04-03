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


def findGroups():
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
    for i in range(len(groups)):
        index.append(i)

    for i in combinations(index, 2):  ##순열로 확인


# print(findGroupsdfs(0, 1))
findGroups()
# print(groups, groupsIndex)
getScore()
