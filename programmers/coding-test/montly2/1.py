def solution(left, right):
    answer = 0
    count = 0
    list = []

    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        list.append(count)
        count = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            answer += left+i
        else:
            answer -= left
    return answer


solution(13, 17)
