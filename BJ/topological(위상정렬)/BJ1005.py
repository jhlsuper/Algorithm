import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    # time = list(map(int, input().split()))
    time = list(input().split())
    arr = []

    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    print(time, arr)
