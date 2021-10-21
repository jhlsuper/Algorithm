def solution(board, skill):
    answer = 0
    for i in skill:
        if i[0] == 1:
            for x in range(i[1], i[3] + 1):

                for y in range(i[2], i[4] + 1):

                    board[x][y] -= i[5]
        else:
            for x in range(i[1], i[3] + 1):

                for y in range(i[2], i[4] + 1):
                    board[x][y] += i[5]
    # print(board)
    for ele in board:
        for j in ele:
            if j>=1:
                answer+=1
    # print(answer)
    return answer


solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
         [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
