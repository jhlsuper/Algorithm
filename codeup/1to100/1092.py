a_list = []
a = int(input())
a_list.append([0 for i in range(23)])


d = list(map(int, input().split()))

for i in d:
    a_list[0][i-1] += 1

for i in range(23):
    print(a_list[0][i], end=" ")
# 파이썬 6092 문제

## list.append([x for i in range(23)])
# list를 x라는 수로 23길이 만큼 채워넣는다. !!!
