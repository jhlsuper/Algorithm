import math


def solution(fees, records):
    answer = []
    dict = {}
    time_dict = {}
    for i in records:
        temp = (i.split(" "))
        time = (temp[0].split(":")[0], temp[0].split(":")[1])
        # print(time)

        if temp[1] not in dict:

            dict[temp[1]] = time
        else:
            # print(dict[temp[1]], time)
            if temp[1] not in time_dict:
                time_dict[temp[1]] = get_time(dict[temp[1]], time)
                # answer_dict[temp[1]] = get_fee(fees, get_time(dict[temp[1]], time))
            else:
                time_dict[temp[1]] += get_time(dict[temp[1]], time)
            del dict[temp[1]]

        # while dict:
    # print(dict)
    for key, value in dict.items():
        if key in time_dict:
            time_dict[key] += get_time(value, ('23', '59'))

        else:
            time_dict[key] = get_time(value, ('23', '59'))


    # print(time_dict)
    time_dict = sorted(time_dict.items(), key=lambda x: x[0])
    # print(time_dict)
    for value in time_dict:
        answer.append(get_fee(fees, value[1]))
    # print(answer_dict)
    # print(answer)
    return answer


def get_time(a, b):
    start_min = int(a[0]) * 60 + int(a[1])

    end_min = int(b[0]) * 60 + int(b[1])
    # print(start_min, end_min ,"times")

    return end_min - start_min


def get_fee(fee, time):
    if time <= fee[0]:
        return fee[1]
    else:
        return fee[1] + math.ceil((time - fee[0]) / fee[2]) * fee[3]


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
