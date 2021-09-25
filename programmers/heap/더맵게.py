import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 1:

        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer
        least = heapq.heappop(scoville)

        if least >= K:
            print(answer)
            return answer
        least2 = heapq.heappop(scoville)
        add = least
        heapq.heappush(scoville, least + (least2 * 2))
        answer += 1

    return -1


solution([1, 2, 3], 11)
