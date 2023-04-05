import sys
from itertools import combinations

global d
global w
global k
global max
global maps
global countli


def checkD():
    # print
    global maps
    global countli
    # print(countli)
    totalCnt = 0

    for i in range(w):

        ##0이면 A 1이면 B

        count = 1
        for j in range(d-1):
            a = maps[j][i]
            b = maps[j + 1][i]
            if countli[j] != -1:
                a = countli[j]
            if countli[j + 1] != -1:
                b = countli[j + 1]
            if a == b:
                count += 1
                if count >= k:
                    break

            else:
                count = 1
        if count < k:
            return False
    return True


def dfs(idx, cnt):
    global max
    if cnt > max:
        return
    if idx == d:
        if checkD():
            if cnt < max:
                max = cnt
        return

    # temp = countli[idx]
    countli[idx] = -1
    dfs(idx + 1, cnt)
    # countli[idx] = temp
    countli[idx] = 0
    dfs(idx + 1, cnt + 1)
    # countli[idx] = temp
    countli[idx] = 1
    dfs(idx + 1, cnt + 1)
    # countli[idx] = temp


T = int(input())

for tc in range(1, T + 1):
    d, w, k = map(int, input().split())
    ## 두께 w 가로크기
    maps = [list(map(int, input().split())) for _ in range(d)]

    max = 1e9
    countli = [-1] * d
    # print(max)
    dfs(0, 0)
    print(f"#{tc} {max}")
