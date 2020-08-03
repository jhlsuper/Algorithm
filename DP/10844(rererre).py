import sys

n = int(sys.stdin.readline())

dp =[]
dp.append([1 for i in range(10)])  #0~9까지 다 1로 채움
for i in range(99):
    dp.append([0 for i in range(10)])
for i in range(99):
    for j in range(10):
        if j>= 1:
            dp[i+1][j-1] += dp[i][j]
        if j<=8:
            dp[i+1][j+1] += dp[i][j]

print(( sum(dp[n-1]) - dp[n-1][0]) % 1000000000)
