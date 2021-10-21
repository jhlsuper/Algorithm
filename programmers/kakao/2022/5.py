from collections import deque


def solution(info, edges):
    answer = 1
    edge = [[] for i in range(len(info))]
    # print(edge)
    visited = [False] * len(info)

    for i in edges:
        edge[i[0]].append(i[1])
    # print(edge)
    # dfs(edge, 0, visited, 0, info)
    answer = bfs(edge, 0, visited, 0, 0, info)
    print(answer)
    return answer


def bfs(graph, start, visited, sheep, wolf, info):
    queue = deque([start])
    max = 0
    index = 0
    visited[start] = True

    while index < 100:

        v = queue.popleft()
        # print(v)
        index += 1
        if info[v] == 0 and visited[v] !=True:
            sheep += 1

        else:
            if visited[v] != True:
                wolf+=1
            queue.append(v)

        for i in graph[v]:
            # print(i)

            if not visited[i]:
                queue.append(i)
                if wolf>= sheep:
                    continue
                visited[i] = True
    return sheep


solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])
