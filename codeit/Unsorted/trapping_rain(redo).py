def trapping_rain(buildings):
    # 코드를 작성하세요
    now_high = 0
    next_high = 0
    total = 0
    for i in buildings:
        if i > now_high:
            now_high = i
        if i < now_high:
            total +=now_high-i




# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))