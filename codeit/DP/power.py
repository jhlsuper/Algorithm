def power(x, y):
    # 코드를 작성하세요. 입력받은 2정 x의 y승을 구한는 문제
    # base case
    if y == 1:
        return x
    elif y == 0:
        return 1
    return(power(x, y//2)*power(x, y-(y//2)))

    # 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

# 코드잇 답


# def power(x, y):
#     if y == 0:
#         return 1

#     subreslut = power(x, y//2)
#     # 문제를 홀수 짝수 경우를 따로 나누다
#     if y % 2 == 0:
#         return subreslut*subreslut
#     else:
#         return x * subreslut*subreslut
