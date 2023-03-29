from itertools import permutations, combinations

T = int(input())
answer = 1e9
maps = []
li = []
for i in range(T):
    li.append(i)

for i in range(T):
    maps.append(list(map(int, input().split())))

for i in permutations(li, T):
    # print(i)
    temp = 0
    if maps[i[-1]][i[0]] ==0:  ##마지막에 가는거가 0일때를 처리를 안해줬다!!!!
        break
    temp += maps[i[-1]][i[0]]
    flag = True
    # print(i[-1], i[0])


    for j in range(T - 1):
        # print(maps[i[j]][i[j + 1]])
        if maps[i[j]][i[j + 1]] == 0:
            flag = False
            break
        temp += maps[i[j]][i[j + 1]]
        if temp > answer:
            flag = False
            break
    # print(temp)
    if temp < answer and flag == True:
        answer = temp
print(answer)
# print(maps)
