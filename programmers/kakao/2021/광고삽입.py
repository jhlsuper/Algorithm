def solution(play_time, adv_time, logs):
    answer = ''
    time = {}
    all_time = []
    adv_second = to_second(adv_time)

    for i in logs:

        start, end = (i.split("-"))[0], i.split("-")[1]
        start_second = to_second(start)
        end_second = to_second(end)
        # print(start_second, end_second)

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
    answer = to_string(max_start)
    sum = 0

    return answer


def find_key(dict, val):
    return next(key for key, value in dict.items() if value == val)


def to_second(mtime):
    temp_time = mtime.split(":")
    second = int(temp_time[0]) * 3600 + int(temp_time[1]) * 60 + int(temp_time[2])
    return second


def to_string(seconds):
    h = seconds // 3600
    h = '0' + str(h) if h < 10 else (h)
    seconds = seconds % 3600
    m = seconds // 60
    m = '0' + str(m) if m < 10 else str(m)
    seconds = seconds % 60
    s = '0' + str(seconds) if seconds < 10 else str(seconds)
    return h + ":" +m+":"+s


solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
