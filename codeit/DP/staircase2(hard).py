#
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    # tabulation 방식으로 푼다
    number_of_ways = [1, 1]
    # 계단 높이가 0이거나 1이면 올라가는 방법은 한가지
    for heigth in range(2, stairs+1):
        number_of_ways.append(0)

        for step in possible_steps:
            if heigth - step >= 0:
                number_of_ways[heigth] += number_of_ways[heigth-step]

    return number_of_ways[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
