import sys
from itertools import  combinations

input = sys.stdin.readline
n, m = map(int, input().split())
# print(n, m)

chicken = []
house = []
distance = []
## 배열에 0 인덱스면 0번째 집에서 [0, 1, 2,3,4    ]번째 치킨집과의 거리
answer = 0
arr = []
for i in range(n):

    # arr[i] = [list(map(int, input().split()))]
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 2:
            chicken.append([i, j])
        if temp[j] == 1:
            house.append([i, j])
    arr.append(temp)

for i in house:
    temp = []
    for j in chicken:
        temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
    distance.append(temp)

answer = (sys.maxsize)
for i in combinations([i for i in range(len(chicken))], m):  ##남아있는 치킨집 이중에서 치킨거리 최소값 구하기
    combiSum = 0
    for house in distance:
        houseMin = sys.maxsize
        for j in i:
            if house[j] < houseMin:
                houseMin = house[j]
        combiSum += houseMin
    if combiSum < answer:
        answer = combiSum
print(answer)

