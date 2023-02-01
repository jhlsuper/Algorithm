A = int(input())
T = int(input())
flag = int(input())
count = 0
index = 0
# 0 뻔 1 데기

n = 2

while(True):
    a = [0, 1, 0, 1]
    for i in range(n):

        a.append(0)

    for i in range(n):

        a.append(1)

    n += 1
    # print(a)
    for i in a:

        if(i == flag):
            count += 1

            if(count == T):
                break
        index += 1
        if(index == A):
            index = 0
    if(count == T):
        break
print(index)
