def maxEvents(arrival, duration):
    result = 0
    tmp = 1
    temp = []

    for x, y in zip(arrival, duration):
        temp.append([x, x+y])
    temp.sort(key=lambda x: (x[1], x[0]))
    print(temp)
    for i in range(len(arrival)):
        if tmp <= temp[i][0]:
            result += 1
            tmp = temp[i][1]
    print(result)
    return result


maxEvents([1, 1, 1, 1, 4], [10, 3, 6, 4, 2])
