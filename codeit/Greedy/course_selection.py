def course_selection(course_list):
    # 코드를 작성하세요.
    sorted_list = sorted(course_list, key=lambda x: x[1])  # 수업이 끝나는 순서로 정렬

    selected = [sorted_list[0]]  # 가장먼저 끝난 수업 듣기

    for course in sorted_list:
        if course[0] > selected[-1][1]:
            selected.append(course)

    return selected


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10),
                        (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
