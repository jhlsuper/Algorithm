
# 3가지 케이스의 경우의 수를 다 더하면
# 현재 입력한 케이스의 경우의수
# n-1 케이스는 1를 더하기 전의 총 케이스
# n-2 케이스는 2를 더해주기전 총 케이스
# n-3 케이스는 3을 더해주기전 총케이스
a = int(input())
output =[]
output.insert(0,0)
output.insert(1,1)
output.insert(2,2)
output.insert(3,4)

for i in range(0, a):
    n = int(input())
    for j in range(4, n+1):
        output.insert(j, output[j-1]+output[j-2]+output[j-3])
    print(output[n])
