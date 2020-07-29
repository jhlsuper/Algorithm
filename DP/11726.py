# 다이나믹 프로그래밍 DP
# 2x(n-1) -> 2 x n 으로 증가할때 한개의 방법만이 증가하므로 2 x(n-1) 방법과 동일
# 2x(n-2) 가 2 x n 으로 증가할때 이것도 한가지

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
dp = [0]*n
def f_dp(n):
    if n==1: return 1
    if n ==2: return 2
    if dp[n-1]: return dp[n-1]
    else:
        dp[n-1] = f_dp(n-1)+ f_dp(n-2)
        return dp[n-1]
print(f_dp(n)%10007)