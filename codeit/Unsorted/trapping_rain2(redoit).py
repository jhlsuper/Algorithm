def trapping_rain(buildings):
    # 코드를 작성하세요
    total_height = 0
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n

    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i-1], buildings[i])

    right_list[-1] = buildings[-1]
    for i in range(n-2, -1, -1):
        right_list[i] = max(right_list[i+1], buildings[i])

    for i in range(n):
        upper_bound = min(right_list[i], left_list[i])

        total_height += max(0, upper_bound - buildings[i])

    return total_height


    # 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
