dp = [0,1,1]
n = int(input())
for i in range(3,91):
    dp.append(dp[i-2] + dp[i-1])

print(dp[n])