def solution(code, day, data):
    answer = []
    dict = {}
    for i in data:
        date = i.split(" ")
        # print(date)
        one_code = date[1]
        price = date[0]
        date2 = date[2]
        actual_code = one_code[5:]
        actual_price = price[6:]
        actual_date = date2[5:13]
        actual_time = int(date2[13:])

        if actual_code == code and actual_date == day:
            # answer.append(actual_price)
            dict[actual_price] = actual_time

    sdict = sorted(dict.items(), key=lambda x: x[1])
    # print(sdict)

    # print(date2[-1, -10])
    for i in sdict:
        # print(i[0])
        answer.append(int(i[0]))
    # print(answer)
    return answer


solution("012345", "20190620", ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014",
                                "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"])
