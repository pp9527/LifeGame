# -*- coding:utf-8 -*-
# author by : 2382852105@qq.com and 2817393972@qq.com

import random
import pygame
import sys


def init_map(rows, cols):
    #初始化指定长宽的地图, rows(int), cols(int), 返回第一张随机细胞状态图
    initial_map = [[0 for i in range(cols)]for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            initial_map[i][j] = random.randint(0, 1)
    return initial_map


# def print_map(every_map):
#     """打印地图"""
#     for i in range(0, len(every_map)):
#         for j in range(0, len(every_map[0])):
#             if every_map[i][j] == 0:
#                 """0表示死细胞 打印□"""
#                 print('□', end="")
#                 """1表示活细胞 打印■"""
#             else:
#                 print('■', end="")
#         print("")


def cell_laws(mov_map):
    #入口参数为一个二维列表，根据生命法则推演出下一张地图并返回
    live_cell_num = 0
    new_map = [[0 for i in range(len(mov_map[0]))]for i in range(len(mov_map))]
    for i in range(0, len(mov_map)):
        for j in range(0, len(mov_map[0])):
            if mov_map[i][j - 1] == 1:
                """左"""
                live_cell_num += 1
            if mov_map[i][(j + 1) % len(mov_map[0])] == 1:
                """右"""
                live_cell_num += 1
            if mov_map[i - 1][j] == 1:
                """上"""
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][j] == 1:
                """下"""
                live_cell_num += 1
            if mov_map[i - 1][j - 1] == 1:
                """上左"""
                live_cell_num += 1
            if mov_map[i - 1][(j + 1) % len(mov_map[0])] == 1:
                """"上右"""
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][j - 1] == 1:
                """下左"""
                live_cell_num += 1
            if mov_map[(i + 1) % len(mov_map)][(j + 1) % len(mov_map[0])] == 1:
                """下右"""
                live_cell_num += 1
            if live_cell_num == 3:
                """周围有三个活细胞，下一状态为活"""
                new_map[i][j] = 1
            elif live_cell_num == 2:
                """周围有两个活细胞，保持原状态"""
                new_map[i][j] = mov_map[i][j]
            else:
                """其他情况下一状态为死"""
                new_map[i][j] = 0
            live_cell_num = 0
    return new_map

def check_int(date):
    #输入的地图长宽的合法性检测, int
    try:
        int(date)
    except ValueError:
        print("你输入的不是数字！")
        sys.exit(0)
    date = int(date)
    if date < 1:
        print("请输入大于一的数：")
        sys.exit(0)
    else:
        return date


def out_map(every_map):
	#入口参数：arr[list][list], 返回演变出的下一张细胞状态图
    pygame.init()
    pygame.display.set_caption('LifeGame')
    screen = pygame.display.set_mode([len(every_map[0]) * 6, len(every_map) * 6])
    screen.fill([255, 255, 255])
    for i in range(0, len(every_map)):
        for j in range(0, len(every_map[0])):
            if every_map[i][j] == 1:
                pygame.draw.rect(screen, [255, 0, 0], [j * 6, 6 * i, 5, 5], 0)
            else:
                pygame.draw.rect(screen, [255, 255, 255], [j * 6, i * 6, 5, 5], 0)
    pygame.display.flip()
    pygame.time.delay(15)
    """程序延迟一段时间"""
    return 1


map_rows = input("输入地图高度：")
map_rows = check_int(map_rows)
"""行数 == 一维列表长度 == 地图高度"""
map_cols = input("输入地图宽度：")
map_cols = check_int(map_cols)
"""列数 == 二维数组长度 == 地图宽度"""
game_map = init_map(map_rows, map_cols)
while 1:
    game_map = cell_laws(game_map)
    out_map(game_map)