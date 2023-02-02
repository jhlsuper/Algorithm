from itertools import combinations
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

nc = []  # 안먹는 것들 리스트
cnt = 0
answer = 0
for i in range(M):
    nc.append(list(map(int, input().split())))

for i in combinations(arr, 3):
    for j in nc:
        if(len(set(j) & set(i)) != 2):
            cnt += 1
    if(cnt == 3):
        answer += 1

    cnt = 0
print(answer)
