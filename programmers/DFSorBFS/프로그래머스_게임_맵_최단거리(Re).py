def reachTheEnd(grid, maxTime):
    dd = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    row = len(grid)
    col = len(grid[0])
    new_grid = []
    check_maps = [[-1 for _ in range(col)] for _ in range(row)]
    check_maps[0][0] = 1
    print(check_maps)

    queue = []
    for i in grid:
        new_grid.append(list(i))
    print(new_grid)
    queue.append([0, 0])
    while queue:
        b, a = queue.pop(0)
        print(b, a)
        for i in range(4):
            dy = b + dd[i][0]
            dx = a + dd[i][1]
            if -1 < dx < col and -1 < dy < row:
                if grid[dy][dx] == '.':
                    if check_maps[dy][dx] == -1:
                        # print(dy, dx)
                        check_maps[dy][dx] = check_maps[b][a]
                        queue.append([dy, dx])
    answer = check_maps[-1][-1]
    print(answer)


# reachTheEnd(['.#', '#.'], 2)
reachTheEnd(['..#', '#.#', '#..'], 3)
