from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for infos in info:
        temp = infos.split(" ")
        key = temp[:-1]
        score = int(temp[-1])

        for i in range(5):
            combi = list(combinations(key, i))
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)
    for key in info_dict.keys():
        info_dict[key].sort()
    print(info_dict)

    for querys in query:
        querys = querys.split(" ")
        query_key = querys[:-1]
        query_score = int(querys[-1])
        # print(query_key)
        ## and 는 최대 3개 까지 있다.
        for _ in range(3):
            query_key.remove("and")
        while "-" in query_key:
            query_key.remove("-")

        ##하나의 string으로 만든다.
        query_key = ''.join(query_key)

        if query_key in info_dict:
            scoreList = info_dict[query_key]
            # print(scoreList)
            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= query_score:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scoreList) - left)
        else:
            answer.append(0)
    # print(answer)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
