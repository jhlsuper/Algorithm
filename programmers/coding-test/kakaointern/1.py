def solution(s):
    dict = {"ze": [0, 4],  "on": [1, 3], "tw": [2, 3], "th": [3, 5], "fo": [4, 4],
            "fi": [5, 4], "si": [6, 3], "se": [7, 5], "ei": [8, 5], "ni": [9, 4]}
    i = 0
    number = "4"
    # print(number.isdigit())
    answer = ''
    # print(dict["ze"][1])
    while i != len(s):
        # for i in range(len(s)):
        if (s[i]).isdigit() == True:
            answer += s[i]
            i += 1
        else:
            answer += str(dict[(s[i]+s[i+1])][0])
            i += dict[s[i]+s[i+1]][1]

    # print(answer)
    return int(answer)


solution("23four5six7")
