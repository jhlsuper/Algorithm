def solution(word):
    answer = 0
    dict = {"E": 1, "I": 2, "O": 3, "U": 4}

    for i in range(len(word)):
        if word[i] == "A":
            answer += 1
        else:
            for j in range(4, i, -1):
                answer += (5 ** (j - 1)) * dict[word[i]]
            answer += dict[word[i]] + 1
    return answer

# 세번째 예제에서 I가 나왔는데
# I가 나오려면
# a e i o u로
# 각각 길이가 1 2 3 4 5인 단어를 만드는 경우의 수
# 2 + 2*5 + 2*5*5 + 2*5*5*5 + 2*5*5*5*5 = 1562
