n = int(input())
li = []

# print(li)
for i in range(n):
    temp = (list(input().split()))
    for k in range(len(temp)):
        temp[k] = int(temp[k])

    li.append(temp)
# print(li)
for i in range(n - 1):
    # print(n-i-1)
    for j in range(n - i - 1):
        # print(n-i-1, j)
        # print(li[n - i - 1][j])
        li[n - i - 2][j] = (li[n - i - 2][j]) + max(li[n - i - 1][j], li[n - i - 1][j + 1])
print(max(li[0]))

