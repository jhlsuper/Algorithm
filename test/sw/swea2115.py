## 수익 8*8  채취한 것의 곱하기
import sys
from itertools import combinations, permutations

input = sys.stdin.readline
comb = []
T = int(input())


def isSafe(x, y):
    temp = 0
    for i in range(M):
        if -1 < y + i < N:
            temp += 1
    return 1 if temp == M else 0


def cal(x, y):
    cap = []
    for i in range(M):
        temp = li[x][y + i]
        cap.append(temp)

    subsum = []
    for j in range(M):
        combs = combinations(cap, M - j)
        for comb in combs:
            if sum(comb) <= C:
                summ = 0
                for k in comb:
                    summ += k ** 2
                subsum.append(summ)
    return max(subsum)


def profit(i, j):
    prof1 = cal(i, j)
    temp = []
    for a in range(i, N):
        k = j + M if a == i else 0
        for b in range(k, N):
            if isSafe(a, b):
                temp.append(cal(a, b))
    return max(temp) + prof1 if temp else 0


for i in range(1, T + 1):
    N, M, C = map(int, input().split())  ## M 벌통갯수, C최대양 10
    li = []
    for j in range(N):
        li.append([0] * N)
    # print(li)
    for j in range(N):
        li[j] = list(map(int, input().split()))
    maxi = 0

    for i in range(N):
        for j in range(N):
            if isSafe(i, j):
                maxi = max(maxi, profit(i, j))
    # print(li, comb)
