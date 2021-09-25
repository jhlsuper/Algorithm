def solution(grid):
    answer = []
    print(len(grid[0]))
    if (len(grid) == 1) and (grid[0] == 1):
        answer.append([1, 1, 1, 1])

        return answer

    for i in grid:
        print(i)
    return answer


# solution(["SL", "LR"])
solution(["S"])
