def solution(play_time, adv_time, logs):
    answer = ''
    play_time = to_string(play_time)
    time = {}
    all_time = [0 for i in range(play_time + 1)]
    adv_second = to_second(adv_time)

    for i in logs:
        start, end = (i.split("-"))[0], i.split("-")[1]
        start_second = to_second(start)
        end_second = to_second(end)
        # print(to_string(start_second), to_string(end_second))
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = i - adv_time + 1
            else:
                if most_view < all_time[i]:
                    most_view = all_time[i]
                    max_time = i - adv_time + 1
    return to_string(max_time)

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
    return h + ":" + m + ":" + s


solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
