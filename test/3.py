## 6*6 게임
## 위치, 마카롱 색깔
import sys


def solution(macaron):
    global arr
    global delete_arr
    arr = []
    global visited
    answer = []
    visited = []
    index = 0

    delete_arr = []

    for i in range(6):
        arr.append([0 for _ in range(6)])
    for i in macaron:
        index += 1
        a, b = 0, 0
        for j in range(6):
            if arr[i[0] - 1][5 - j] == 0:
                arr[i[0] - 1][5 - j] = i[1]
                a = i[0] - 1
                b = 5 - j
                break
        if index >= 3:
            delete_arr = []
            visited = []
            search([a, b])
            if len(delete_arr) >= 3:
                for z in delete_arr:
                    arr[z[0]][z[1]] = 0
                arr = clear(arr)
                for i in range(6):
                    for j in range(6):
                        if arr[i][j] != 0:
                            delete_arr = []
                            visited = []
                            search([i, j])
                            if len(delete_arr) >= 3:
                                for z in delete_arr:
                                    arr[z[0]][z[1]] = 0
                                arr = clear(arr)

    for i in range(6):
        temp = ""
        for j in range(6):
            temp += str(arr[j][i])
        answer.append(temp)

    return answer


def search(index):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dx, dy = 0, 0
    visited.append(index)
    delete_arr.append(index)

    for i in d:

        dx = index[0] + i[0]
        dy = index[1] + i[1]
        if 0 <= dx <= 5 and 0 <= dy <= 5 and [dx, dy] not in visited:
            if arr[dx][dy] == arr[index[0]][index[1]]:
                search([dx, dy])


def clear(arr):
    re_arr = []
    for i in arr:
        temp = []
        for j in i:
            if j != 0:
                temp.append(j)
        add_temp = [0 for _ in range(6 - len(temp))]
        re_arr.append(add_temp + temp)
    return re_arr


solution([[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]])
