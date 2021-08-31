def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        # print(i)
        total += i * price
    # print(total)
    if money-total >= 0:
        return 0
    else:
        return -(money-total)

    # return answer


solution(3, 20, 4)
