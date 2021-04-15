def solution(a, edges):
    edges_count = []
    for i in range(len(a)):
        edges_count.append(0)

    for i in range(len(a)-1):
        for j in edges[i]:
            edges_count[j] += 1
    # print(edges_count)
    if sum(a) == 0:
        answer = 0

    else:
        return -1
    answer = -2
    return answer


solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
