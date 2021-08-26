def solution(play_time, adv_time, logs):
    answer = ''
    time = {}
    adv_second =to_second(adv_time)

    for i in logs:

        start, end = (i.split("-"))[0], i.split("-")[1]
        start_second = to_second(start)
        end_second = to_second(end)
        print(start_second, end_second)

        for j in range(start_second, end_second):
            if j not in time:
                time[j] = 1
            else:
                time[j] += 1

    max_value = max(time.values())
    max_start = (find_key(time, max_value))
    temp = max_start
    while time[temp] == max_value:
        temp += 1
    print(max_start, temp - 1)
    sum =0


    # hour = int((temp-1) / 3600)
    # minute = int(((temp-1) % 3600) / 60 % 60)
    # print(hour,minute)

    return answer


def find_key(dict, val):
    return next(key for key, value in dict.items() if value == val)


def to_second(mtime):

    temp_time = mtime.split(":")
    second = int(temp_time[0]) * 3600 + int(temp_time[1]) * 60 + int(temp_time[2])
    return second


solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
