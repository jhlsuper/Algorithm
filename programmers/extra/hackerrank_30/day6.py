a = int(input())
list = []
first = ''
second = ''
for i in range(a):
    list.append(input())
for word in list:
    for j in range(len(word)):
        if j % 2 == 0:
            first += word[j]
        else:
            second += word[j]
    print(first, second)
    first = ''
    second = ''
# print(list)
