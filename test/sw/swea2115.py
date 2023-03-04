## 수익 8*8  채취한 것의 곱하기
import sys
from itertools import combinations, permutations
input = sys.stdin.readline

T = int(input())
N, M, C = map(int, input().split())  ## M 벌통갯수, C최대양 10

for i in range(T):
    li = []
    for j in range(N):
        li.append([0] * N)
    # print(li)
    for j in range(N):
        li[j] = list(map(int, input().split()))

    for j in combinations(3, 2):
        print(j)