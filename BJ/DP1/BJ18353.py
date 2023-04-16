# 앞쪽의 병사는  뒤쪽에 있는 병사 보다 높아야된다.

N = int(input())

answer = 0
li = [int(i) for i in input().split()]

dp = [1] * N

for i in range(N):
    for j in range(i):
        print(dp)
        if li[i] < li[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(len(li)-max(dp))
