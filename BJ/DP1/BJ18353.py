# 앞쪽의 병사는  뒤쪽에 있는 병사 보다 높아야된다.

N = int(input())
dp = [0] * (N + 1)
answer = 0
li = (input().split())
index = 0
for i in range(N):
    index = N - 1 - i
    print(li[index])

