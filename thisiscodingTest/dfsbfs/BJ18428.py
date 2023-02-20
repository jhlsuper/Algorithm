import sys
import copy
from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
flag = False
empty = []
teachers = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':  ##비어있는곳 저장
            empty.append((i, j))
        if arr[i][j] == 'T':
            teachers.append((i, j))  ## 선생님 정보 저장
def bfs():
    dq = deque([])
    for a, b in teachers:
        for i in range(4):
            dq.append((a, b, i))
    while dq:
        xx, yy, dd = dq.popleft()
        nx = xx + dx[dd]
        ny = yy + dy[dd]
        if 0 <= nx < N and 0 <= ny < N:
            if copy_arr[nx][ny] == 'S':
                return False
            elif copy_arr[nx][ny] == 'X':
                dq.append((nx, ny, dd))
    return True





for i in combinations(empty, 3):
    copy_arr = copy.deepcopy(arr)
    for j in i:
        copy_arr[j[0]][j[1]] ='O'
    if bfs():
        print("YES")
        flag = True
        break
if not flag:
    print("NO")




