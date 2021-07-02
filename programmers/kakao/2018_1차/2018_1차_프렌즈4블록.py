def solution(m, n, board):
    answer = 0

    board_list = [[-1] * n for row in range(m)]

    a = 0
    for i in range(m):
        for j in range(n):
            board_list[i][j] = board[i][j]
    print(board_list)
    while a < m:
        temp_list = []
        board_list, answer = del_block(m, n, board_list,answer)

        print(board_list)
        move_down(m, n, board_list)
        a += 1

    # print(answer)
    return answer


def del_block(m, n, board, answer):
    temp_list = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != -1:
                # print(board[i][j:j + 2])
                if board[i][j:j + 2] == board[i + 1][j:j + 2]:

                    for x in range(i, i + 2):
                        for y in range(j, j + 2):
                            if [x, y] not in temp_list:
                                temp_list.append([x, y])
                                answer += 1

    for i in temp_list:
        board[i[0]][i[1]] = -1
    return board, answer


def move_down(m, n, board):
    for i in range(m - 1, 0, -1):
        for j in range(n):
            # print(i, j)
            if board[i][j] == -1:
                board[i][j] = board[i - 1][j]
                board[i - 1][j] = -1
    return board


solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"])
