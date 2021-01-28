def staircase(n):
    # 코드를 작성하세요.
    # 인풋 값의 N을 2와 1로 더해서 채우는 갯수를 구하라.
    dp = [0, 1, 2]
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[n]


# 코드잇에서 푼 방법
# 시간 복잡도 O(n)
"""
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
"""
# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
