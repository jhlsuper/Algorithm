import heapq


def solution(n, s, a, b, fares):
    answer = []

    dic = {}
    for i in range(n):
        dic[i + 1] = {}
    for j in fares:
        dic[j[0]][j[1]] = j[2]
        dic[j[1]][j[0]] = j[2]
    print(dic)
    candidate = dijkstra(dic, s)
    # print(candidate)
    # 그냥 따로따로 출발지에서 출발하는 경우
    answer.append(candidate[a] + candidate[b])
    for i in range(1, n + 1):
        if i == s:
            continue
        mid = i
        # print(dic)
        temp = dijkstra(dic, mid)
        answer.append(candidate[mid] + temp[a] + temp[b])
        # print(temp)
    return min(answer)


# 다익스트라 사용

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # print(distances)
    queue = []
    heapq.heappush(queue, [distances[start], start])
    # print(queue)
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    # print(distances)
    return distances


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
