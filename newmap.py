"""
cell_laws
"""


def cell_laws(mov_map):
    """
    :param mov_map: list
    :return: list
    """
    # 入口参数为一个二维列表，根据生命法则推演出下一张地图并返回
    diction = {
        "left": (0, -1),
        "write": (0, 1),
        "up": (-1, 0),
        "down": (1, 0),
        "up_left": (-1, -1),
        "up_write": (-1, 1),
        "down_left": (1, -1),
        "down_write": (1, 1)
    }
    row = len(mov_map)
    col = len(mov_map[0])
    live_cell_num = 0
    new_map = [[0 for i in range(len(mov_map[0]))]for i in range(len(mov_map))]
    for i in range(0, row):
        for j in range(0, col):
            for dire in diction:
                t_row = (i + diction[dire][0]) % len(mov_map)
                t_col = (j + diction[dire][1]) % len(mov_map[0])
                if mov_map[t_row][t_col] == 1:
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
