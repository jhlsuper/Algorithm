## 경쟁적 전염

## N*N 크기의 시험관  1~K번의 바이러스
# 모든 바이러스는 1초마다 상하좌우 증식 번호가 낮은 종류 부터 먼저 증식

# xy에 존재하는 바이러스 출력 ,  존재 x -> 0
## 0,0 좌표가 1,1
## S 초 뒤에 x,y 에 존재하는 바이러스
import sys
from collections import deque

global dict
global count
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

input = sys.stdin.readline
N, K = map(int, input().split())
li = []

count = N * N

arr = [[0] * N for _ in range(N)]  ## N*N 0으로 초기화된 배열

for i in range(N):

    temp = list(map(int, input().split()))

    for j in range(N):

        arr[i][j] = temp[j]
        if temp[j] != 0:
            count -= 1

            li.append((temp[j], 0, i, j))  ##바이러스 종류, 시간, ,x ,y
li.sort()
q = deque(li)
S, X, Y = map(int, input().split())

# global tempDict
# tempDict = {}
#
#
# def spr(x, y, key):
#     global count
#     for i in range(4):
#         newX = x + dx[i]
#         newY = y + dy[i]
#         if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] == 0:
#             arr[newX][newY] = key
#             count -= 1
#             # dict[key].append((newX, newY))  ##여기서 add되서 계속 일어난다.
#             if tempDict.get(key):
#                 tempDict[key].append((newX, newY))
#             else:
#                 tempDict[key] = [(newX, newY)]
#
#
# for i in range(S):
#     # print(i)
#     if count == 0:
#         break
#     templi = []
#     for key in dict:
#         temp = dict.get(key)
#         # print(temp, key)
#         for j in temp:
#             # print(j[0], j[1], key)
#             templi.append((j[0], j[1], key))
#     for k in templi:
#         spr(k[0], k[1], k[2])
#     dict = tempDict
#     tempDict={}
#
while q:
    if count == 0:
        break
    key, time, x, y, = q.popleft()
    if time == S:
        break
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] == 0:
            arr[newX][newY] = key
            count-=1
            q.append((key, time + 1, newX, newY))
print(arr[X - 1][Y - 1])
