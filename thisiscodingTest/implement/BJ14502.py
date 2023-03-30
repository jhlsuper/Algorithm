from itertools import combinations, permutations
import copy
from collections import deque

N, M = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# maps = [list(map(int, input().split())) for _ in range(N)]
maps = []
virus = []
empty = []
lists = []
answer = 0


def spread(cmaps):
    # print(cmaps)
    visited = [[False] * M for _ in range(N)]
    # print(visited)
    q = deque()
    for i in virus:
        # print(i)
        q.append(i)
    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and cmaps[nx][ny] == 0:
                visited[nx][ny] = True
                cmaps[nx][ny] = 2
                q.append((nx, ny))
    count = 0

    for i in range(N):
        for j in range(M):
            if cmaps[i][j] == 0:
                count += 1
    # print(count)
    return count


for i in range(N):
    temp = list(map(int, input().split()))
    maps.append(temp)
    for j in range(M):
        if temp[j] == 2:
            virus.append((i, j))

        if temp[j] == 0:
            empty.append((i, j))
# print(maps)
# print(empty)
for i in range(len(empty)):
    lists.append(i)
# print(lists)
for i in combinations(lists, 3):
    mapCopy = copy.deepcopy(maps)
    # print(i)
    for j in i:
        x = empty[j][0]
        y = empty[j][1]
        # print(x,y)
        mapCopy[x][y] = 1
    tempAnswer = spread(mapCopy)
    # break;
    if answer < tempAnswer:
        answer = tempAnswer
print(answer)
# break
