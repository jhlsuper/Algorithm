def solution(scores):
    answer = ''

    for i in range(len(scores)):

        if scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i]):
            scores[i][i] = 0
        b = [z[i] for z in scores]  ##colume을 출력하는 방법
        if 0 in b:
            b.remove(0)
        temp = sum(b) / len(b)
        answer += getgrade(temp)
    print(answer)
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


solution(
    [[70, 49, 90], [68, 50, 38], [73, 31, 100]])
