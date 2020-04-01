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


def cell_laws(mov_map):
    #入口参数为一个二维列表，根据生命法则推演出下一张地图并返回


def check_int(date):
    #输入的地图长宽的合法性检测, int


def out_map(every_map):
	#入口参数：arr[list][list], 返回演变出的下一张细胞状态图