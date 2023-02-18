def solution(n, weak, dist):
    answer = 0
    longest = max(weak) -min(weak)
    if max(dist) >= longest:
        return 1
    else:
        return 2


    # return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
