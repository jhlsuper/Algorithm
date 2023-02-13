from itertools import combinations

a, b = map(int, input().split())
arr = []
answer = 0
temp = list(map(int, input().split()))
# print(temp)
arr = [i for i in range(len(temp))]

for i in combinations(arr, 2):
    # print(i)
    # print((temp[i[0]], temp[i[1]]))
    if temp[i[0]] != temp[i[1]]:
        answer += 1
print(answer)
