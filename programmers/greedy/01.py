def solution(n, lost, reserve):
    lost = sorted(lost)
    # reserve = sorted(reserve)
    answer = n-len(lost)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer = answer+1
            continue
        for j in reserve:
            if j ==i-1:
                answer =answer +1
                reserve.remove(j)
                break
            elif j==i+1:
                if j in lost:
                    break
                answer =answer+1
                reserve.remove(j)
                break


    return(answer)
