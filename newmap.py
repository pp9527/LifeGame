def cell_laws(mov_map):
    # 入口参数为一个二维列表，根据生命法则推演出下一张地图并返回
    live_cell_num = 0
    new_map = [[0 for i in range(len(mov_map[0]))]for i in range(len(mov_map))]
    for i in range(0, len(mov_map)):
        for j in range(0, len(mov_map[0])):
            if mov_map[i][j - 1] == 1:
                # 左
                live_cell_num += 1
            if mov_map[i][(j + 1) % len(mov_map[0])] == 1:
                # 右
                live_cell_num += 1
            if mov_map[i - 1][j] == 1:
                # 上
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][j] == 1:
                # 下
                live_cell_num += 1
            if mov_map[i - 1][j - 1] == 1:
                # 上左
                live_cell_num += 1
            if mov_map[i - 1][(j + 1) % len(mov_map[0])] == 1:
                # 上右
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][j - 1] == 1:
                # 下左
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][(j + 1) % len(mov_map[0])] == 1:
                # 下右
                live_cell_num += 1
            if live_cell_num == 3:
                # 周围有三个活细胞，下一状态为活
                new_map[i][j] = 1
            elif live_cell_num == 2:
                # 周围有两个活细胞，保持原状态
                new_map[i][j] = mov_map[i][j]
            else:
                # 其他情况下一状态为死
                new_map[i][j] = 0
            live_cell_num = 0
    return new_map
