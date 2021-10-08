def solution(scores):
    answer = ''
    len1 = len(scores[0])

    for i in range(len(scores)):
        temp = []
        self_score = scores[i][i]
        # print(self_score)
        for j in range(len1):
            temp.append(scores[j][i])
        # print(temp)
        if self_score == max(temp) or self_score == min(temp):
            if temp.count(self_score) == 1:
                temp.remove(self_score)
        score = sum(temp) / len(temp)
        answer += getgrade(score)

    return answer


def getgrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif 70 > score >= 50:
        return "D"
    elif 50 > score:
        return "F"