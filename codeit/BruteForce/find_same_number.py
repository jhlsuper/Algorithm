def find_same_number(some_list):
    # 코드를 쓰세요
    length = len(some_list)
    a = []
    for i in range(length):
        a.append(1)

    for i in some_list:
        a[i-1] = a[i-1]+1
        if a[i-1] == 3:
            return i

# ㅡㅡㅡㅡㅡㅡㅡㅡ코드잇 풀이 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 이 방법으로 푸는게 훨씬 빠름 내 풀이는 약간 잘못됨

    elements_seen_so_far = {}
    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다.
        if element in elements_seen_so_far:
            return element
        elements_seen_so_far[element] = True


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
