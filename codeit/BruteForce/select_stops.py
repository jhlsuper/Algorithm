def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    # 리스트의 값들이 약수터가 있는 위치 마지막원소가 정상 capacity는 물통의 용량
    a = []
    water_record = capacity-water_stops[0]
    for i in range(len(water_stops)-1):

        distance = water_stops[i+1]-water_stops[i]

        if water_record-distance < 0:
            a.append(water_stops[i])
            water_record = capacity-distance
        elif water_record-distance == 0:
            a.append(water_stops[i+1])
            water_record = capacity
        else:
            water_record = water_record-distance
    a.append(water_stops[-1])
    return a

    # ㅡㅡㅡㅡㅡ코드잇에서 푼 방법 ㅡㅡㅡㅡㅡㅡㅡㅡ
    # stop_list = []
    # prev_stop = 0  # 마지막에 들른 약수터 위치

    # for i in range(len(water_stops)):
    #     # i 지점까지 갈수 없다면 , i-1 지점 약수터를 들른다.
    #     if water_stops[i]-prev_stop > capacity:
    #         stop_list.append(water_stops[i-1])
    #         prev_stop = water_stops[i-1]


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
