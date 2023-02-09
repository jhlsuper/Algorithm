N = int(input())
start = 0
end = 0
answer = 0

arrEnd = []

for i in range(N):
    a, b = map(int, input().split())
    arrEnd.append([a, b])

arrEnd.sort(key=lambda x: (x[1], x[0]))

start = arrEnd[0][0]
end = arrEnd[0][1]

index = 0
if end != 0:
    answer += 1

for i in range(index + 1, len(arrEnd)):
    # print(arrEnd[i])
    if int(arrEnd[i][0]) >= end and arrEnd[i]:
        end = arrEnd[i][1]
        index = i
        answer += 1

print(answer)
