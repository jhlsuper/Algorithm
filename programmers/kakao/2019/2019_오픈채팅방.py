def solution(record):
    answer = []
    dictionary = {}

    for i in record:
        temp = i.split(" ")

        # print(temp)
        if i[0] == 'E':
            dictionary[temp[1]] = temp[2]
            answer.append([temp[1], "님이 들어왔습니다."])

        if i[0] == 'L':
            answer.append([temp[1], "님이 나갔습니다."])

        if i[0] == 'C':
            dictionary[temp[1]] = temp[2]
    for z in range(len(answer)):
        answer[z][0] = dictionary[answer[z][0]]
        answer[z] = answer[z][0] + answer[z][1]

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
