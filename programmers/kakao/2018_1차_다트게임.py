def solution(dartResult):
    a = list(dartResult)
    answer = []
    score_list = []

    for i in range(len(a)):
        if a[i] == '1' and a[i + 1] == '0':
            score_list.append('10')
        elif a[i] == '0' and a[i - 1] == '1':
            continue
        else:
            score_list.append(a[i])

    for i in range(1, len(score_list)):
        if score_list[i] == 'S':
            answer.append(int(score_list[i - 1]))
        elif score_list[i] == 'D':
            answer.append(int(score_list[i - 1]) ** 2)
        elif score_list[i] == 'T':
            answer.append(int(score_list[i-1]) ** 3)

        if score_list[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif score_list[i] == '#':
            answer[-1] = answer[-1] * (-1)
    return sum(answer)

solution("1S2D*3T")
