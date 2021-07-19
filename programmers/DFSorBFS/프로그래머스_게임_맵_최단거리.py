from collections import deque


def reachTheEnd(grid, maxTime):
    dd = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ROW = len(grid)
    COL = len(grid[0])
    new_gird = []
    check_maps = [[-1 for _ in range(COL)] for _ in range(ROW)]
    check_maps[0][0] = 1
    print(check_maps)
    queue = []
    for i in grid:
        new_gird.append(list(i))
    print(new_gird)
    queue.append([0, 0])

    while queue:
        b, a = queue.pop(0)
        for i in range(4):
            dy = b + dd[i][0]
            dx = a + dd[i][1]
            if -1 < dx < COL and -1 < dy < ROW:
                if grid[dy][dx] == '.':
                    if check_maps[dy][dx] == -1:
                        print(dy, dx)
                        check_maps[dy][dx] = check_maps[b][a] + 1
                        queue.append([dy, dx])
    answer = check_maps[-1][-1]
    print(answer)
    if answer == -1:
        return "No"
    if maxTime >= answer:
        return "Yes"
    else:
        return "No"

    # return answer


# reachTheEnd(['..##', '#.##', '#...'], 5)
reachTheEnd(['.#', '#.'], 2)
