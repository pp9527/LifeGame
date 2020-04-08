# -*- coding:utf-8 -*-
# author by : 2382852105@qq.com and 2817393972@qq.com

import pygame
import sys
import outmap
import check
import newmap
import init


map_rows = input("输入地图高度：")
map_rows = check.check_int(map_rows)
# 行数 == 一维列表长度 == 地图高度
map_cols = input("输入地图宽度：")
map_cols = check.check_int(map_cols)
# 列数 == 二维数组长度 == 地图宽度
game_map = init.init_map(map_rows, map_cols)
while 1:
    game_map = newmap.cell_laws(game_map)
    outmap.out_map(game_map)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
