import sys
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def cnt_length():
    tmp = deepcopy(arr)
    cnt =0
    length = 0
    for i in range(Q_len):
        if Q_dir[i] <0:
            continue
        if not check(Q[i][0], Q[i][1],Q_dir[i],tmp):
            continue
        cnt +=1
        di=Q[i][0]+ D[Q_dir][i]][0]

def check(i, j, d, arr):
    di = i + D[d][0]
    dj = j + D[d][1]
    while 0 <= di < N and 0 <= dj < N:
        if arr[di][dj] == 1:
            return False
        di += D[d][0]
        dj += D[d][1]
    return True


T = int(input())
for t in range(1, T):
    N = int(input())
    Q = []
    fix = 0
    # li = [list(map(int, input().split())) for _ in range(N)]
    arr = [[] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            arr[i].append(temp[j])
            if temp[j] == 1:
                Q.append([i, j])
                # if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                #     fix += 1
                # else:
                #     Q.append((i, j))
    Q_len = len(Q)
    Q_dir = [0] * Q_len
    max_cnt = 0
    min_len = 1e9
    solve(0)
