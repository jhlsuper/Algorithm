import sys
from itertools import combinations, permutations

input = sys.stdin.readline
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# print(arr)
for i in combinations(range(N),2):
    print(i)
for i in combinations(range(N)):
    print(i)