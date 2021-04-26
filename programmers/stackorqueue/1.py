def solution(bridge_length, weight, truck_weights):
    answer = 0

    list = [0]*bridge_length

    while list:
        answer += 1
        list.pop(0)
        # print(list)
        if truck_weights:
            if sum(list) + truck_weights[0] <= weight:
                list.append(truck_weights.pop(0))
                # print(list)

            else:
                list.append(0)
                # print(list)

    # print(answer)

    return answer


solution(2, 10, [7, 4, 5, 6])
