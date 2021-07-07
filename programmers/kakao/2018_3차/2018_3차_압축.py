def solution(msg):
    ascii_list = []
    answer = []
    ascii_list.append('0')
    msg_list = list(msg)
    print(msg_list)

    for i in range(1, 26):
        ascii_list.append(chr(i + 64))
    print(ascii_list)
    for i in range(len(msg)):
        j = 0
        if msg_list[i] != '0':
            while msg_list[i:i + j + 1] in ascii_list:
                j += 1
                print(msg_list[i:i + j])
            if msg_list[i:i + j + 2] not in ascii_list:
                ascii_list.append(msg_list[i:i + j + 2])
                print(msg_list)
                for z in range(j):
                    msg[i + j] = '0'

            # if msg_list[i:i + 2] not in ascii_list and msg_list[i] in ascii_list:
            #     ascii_list.append(msg[i:i + 2])
            #     answer.append(ascii_list.index(msg_list[i]))
            #     msg_list[i] = '0'
            # if msg_list[i:i + 2] in ascii_list:
            #     answer.append(ascii_list.index(msg_list[i:i + 2]))
            #     ascii_list.append(msg_list[i:i + 3])

    print(ascii_list)
    print(answer)
    return answer


solution("KAKAO")
