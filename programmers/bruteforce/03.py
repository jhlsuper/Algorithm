def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    x = sum

    temp = []
    # while (x >= y):
    for i in range(sum, 0, -1):
        if sum % i == 0:
            y = sum/i
            if (i >= y) and (i-2)*(y-2) == yellow:
                temp.append([i, int(y)])
    print(temp[-1])
    # return temp[-1]


solution(50, 22)
