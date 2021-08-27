from itertools import combinations


def solution(p, q):
    answer = []

    for i in range(len(p)):
        bo = True
        add = {}
        for number in p[i]:
            add[number] = 1
        temp = (list(combinations((p[i]), 2)))
        for j in temp:
            add[sum(j)] = 1
        print(add)

        for numbers in q[i]:
            if numbers not in add:
                bo = False
                answer.append(False)
                break
            else:
                continue
        if bo:
            answer.append(True)

    # print(answer)
    return answer


solution([[4, 3, 3], [1, 2, 3], [3, 2, 4]], [[5, 5], [5, 1], [1, 8]])
