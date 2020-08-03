# n-1의 케이스는 1을 더하기 전의 총 케이스 값
# n-2의 케이스는 2를 더하기 전의 총 케이스 값
# n-3의 케이스는 3을 더해주기전의 총 케이스 값

# n이 5라고 하면 총 케이스는 4의 총 케이스  +  3의 총케이스 + 2의 총케이스이다.

n = int(input())

output= []

output.insert(0,0)  # 0값에 값을 넣어줘야지 index out of range 에러가 안뜸
output.insert(1,1)
output.insert(2,2)
output.insert(3,4)

for i in range(0,n):
    t = int(input())
    for j in range(4, t+1):
        output.insert(j,output[j-1]+output[j-2]+output[j-3])
    print(output[t])