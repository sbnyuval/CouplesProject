import pygame
import consts
import Screen
board = []
def create():
    for row in range(consts.BOARD_ROWS):
        row = []
        for col in range(consts.BOARD_COLS):
            row.append("EMPTY")
        board.append(row)
    return board
for row in create():
    print(row)
    print()
def Loading_assets():
    soldier_image = pygame.image.load(consts.SOLDIER_IMG)
    soldier_resized = pygame.transform.scale(
        soldier_image, (consts.SOLDIER_BODY_WIDTH, consts.SOLDIER_BODY_HEIGHT)
    )
    flag_image = pygame.image.load("flag.png")
    flag_resized = pygame.transform.scale(
        flag_image, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT)
    )
    grass_image = pygame.image.load("grass.png")
    grass_resized = pygame.transform.scale(
        grass_image, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT)
    )
    return soldier_resized, flag_resized, grass_resized