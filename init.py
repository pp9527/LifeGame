"""
init
"""
import random


def init_map(rows, cols):
    """
    :param rows: int
    :param cols: int
    :return: list
    """
    if rows <= 0 or rows > 100 or cols <= 0 or cols > 100:
        return -1
    # 初始化指定长宽的地图, rows(int), cols(int), 返回第一张随机细胞状态图
    initial_map = [[0 for i in range(cols)]for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            initial_map[i][j] = random.randint(0, 1)
    return initial_map
