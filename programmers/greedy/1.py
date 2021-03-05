def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    answer = n-len(lost)
    print(lost)
    print(reserve)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer = answer+1
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer = answer + 1
            continue

    return(answer)


solution(5, [4, 2], [3])
