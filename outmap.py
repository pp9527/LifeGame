"""
print
"""
import pygame


def out_map(every_map):
    """
    :param every_map:list
    :return: list
    """
    # 入口参数：arr[list][list], 返回演变出的下一张细胞状态图
    row = len(every_map)
    col = len(every_map[0])
    pygame.init()
    pygame.display.set_caption('life_game')
    screen = pygame.display.set_mode([len(every_map[0]) * 6, len(every_map) * 6])
    screen.fill([255, 255, 255])
    for i in range(0, row):
        for j in range(0, col):
            if every_map[i][j] == 1:
                pygame.draw.rect(screen, [0, 0, 255], [j * 6, 6 * i, 5, 5], 0)
            else:
                pygame.draw.rect(screen, [255, 255, 255], [j * 6, i * 6, 5, 5], 0)
    pygame.display.flip()
    pygame.time.delay(15)
    # 程序延迟一段时间
    return 1
