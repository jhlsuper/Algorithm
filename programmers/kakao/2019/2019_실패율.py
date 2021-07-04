def solution(N, stages):
    answer = []
    answer_list = []
    real_answer = []

    done = [0] * (N + 1)
    not_done = [0] * (N + 1)
    for i in stages:

        not_done[i - 1] += 1

        for j in range(i):
            done[j] += 1

    for i in range(N):
        if done[i] == 0:
            answer_list.append([i, 0])
        else:
            answer_list.append([i, not_done[i] / done[i]])
    answer_list.sort(key=lambda x: x[1], reverse=True)
    for i in answer_list:
        real_answer.append(i[0] + 1)
    print(real_answer)
    return real_answer


solution(4, [4, 4, 4, 4, 4])
