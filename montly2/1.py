def solution(absolutes, signs):
    answer = 0
    yang = []
    umm = []
    for i, j in zip(absolutes, signs):
        if j == True:
            yang.append(i)
            answer += i
        elif j == False:
            umm.append(i)
            answer -= i

    return answer


solution([4, 7, 12], [True, False, True])
