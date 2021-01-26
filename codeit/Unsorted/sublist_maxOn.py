def sublist_max(profits):
    # 코드를 작성하세요.
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다.
        max_check = max(max_check + profits[i], profits[i])
        # 다음요소를 더했을때 지금 까지의 max보다 큰지 구분
        max_profit_so_far = max(max_profit_so_far, max_check)
    return max_profit_so_far
    # 시간 복잡도 O(n) 아 너무 싱크빅이다.


    # 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
