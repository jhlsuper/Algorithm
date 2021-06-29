def solution(m, n, board):
    answer = 0

    board_list = [[0] * n for row in range(m)]

    for i in range(m):
        for j in range(n):
            board_list[i][j] = board[i][j]

    print(board_list)

    del_block(m, n, board_list)

    return answer


def del_block(m, n, board):
    temp_list = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                # print(board[i][j:j + 2])
                if board[i][j:j + 2] == board[i + 1][j:j + 2]:
                    print(board[i][j:j + 2], board[i + 1][j:j + 2])
                    for x in range(i, i + 2):
                        for y in range(j, j + 2):
                            if [x, y] not in temp_list:
                                temp_list.append([x, y])

                    print(temp_list)
    for i in temp_list:
        # print(i[0], i[1])
        board[i[0]][i[1]] = '0'

    print(board)


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
