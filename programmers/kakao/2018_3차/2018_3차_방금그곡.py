def solution(m, musicinfos):
    answer = ''
    answer_list = []
    time = [(int(time[6:8]) - int(time[:2])) * 60 + (int(time[9:11]) - int(time[3:5])) for time in musicinfos]

    for i in range(len(musicinfos)):
        note = musicinfos[i].split(",")[-1]
        name = musicinfos[i].split(",")[2]
        # print(note)

        if len(note) < time[i]:
            note *= time[i] // len(note)

        else:
            if m in note[len(time)]:
                answer_list.append(name)
        if m in note:
            answer_list.append([name, time[i]])
    sorted_answer_list = sorted(answer_list, key=lambda x: x[1])
    if len(sorted_answer_list) == 0:
        answer = '(None)'
    else:
        answer = sorted_answer_list[-1][0]
    # print(answer)
    return answer


solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
