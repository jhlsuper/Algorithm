N = int(input())
li = []

for i in range(N):
    li.append(int(input()))
answer = 0
li = sorted(li)

if len(li) == 1:
    print(0)
    exit(0)
else:

    for i in range(len(li) - 1):
        temp = 0
        print("ii", i)
        print(li)
        temp = li[i] + li[i + 1]
        li[i + 1] = temp
        # print(temp)
        answer += temp

print(answer)
