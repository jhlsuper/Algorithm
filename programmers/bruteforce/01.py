def solution(answers):
    answer = []
    i = 0
    # count1, count2, count3 = 0, 0, 0
    list1 = [0, 0, 0]
    lost1 = [1, 2, 3, 4, 5]
    lost2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lost3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == lost1[i % 5]:
            list1[0] += 1
        if answers[i] == lost2[i % 8]:
            list1[1] += 1
        if answers[i] == lost3[i % 10]:
            list1[2] += 1

    for lost, score in enumerate(list1):
        if score == max(list1):
            answer.append(lost+1)
    return answer

    # return answer
solution([1, 2, 3, 4, 5])
