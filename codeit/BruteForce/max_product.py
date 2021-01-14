def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    a = len(left_cards)
    b = len(right_cards)
    c = []
    for i in range(a):
        x = left_cards[i]
        for j in range(b):
            y = right_cards[j]
            c.append(x * y)
    return max(c)


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
