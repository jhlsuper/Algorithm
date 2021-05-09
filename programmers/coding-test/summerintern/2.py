def solution(t, r):
    answer = []
    dict = {}
    i = 0
    j = 0
    for a, b in zip(t, r):
        dict[b] = [a, i]
        i += 1
    # print(dict)
    sdict = sorted(dict.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

    # print((sdict[0])[1][0])
    # print((sdict[1])[1][0])
    while sdict:
        # print(sdict)
        if len(sdict) == 1:
            answer.append(sdict[0][1][1])
            del sdict
            break

        # if (sdict[0])[1][0] == (sdict[1])[1][0]:
        #     (sdict[1])[1][0] += 1
        index = (sdict[0])[1][1]
        answer.append(index)
        del sdict[0]
        for i in sdict:
            if i[1][0] == j:
                i[1][0] += 1

        sdict = sorted(sdict, key=lambda x: (x[1][0], x[1][1], x[0]))
        j += 1
    # index += 1
    # print(sdict)
    # for i in sdict:
    #     answer.append(i[1][1])
    #     del sdict[0]
    # print(answer)
    return answer


solution([0, 1, 3, 0], [0, 1, 2, 3])
