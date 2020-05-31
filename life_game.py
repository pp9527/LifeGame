# -*- coding:utf-8 -*-
# author by : 2382852105@qq.com and 2817393972@qq.com
"""
main
"""
import sys
import pygame
import out_map
import check
import new_map
import init

map_rows = input('input height：')
map_rows = check.check_int(map_rows)
map_cols = input('input width：')
map_cols = check.check_int(map_cols)
game_map = init.init_map(map_rows, map_cols)
while 1:
    game_map = new_map.cell_laws(game_map)
    out_map.out_map(game_map)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
