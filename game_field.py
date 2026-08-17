import random

import pygame
import consts
import Screen
board = []
def create_board():
    for row in range(consts.BOARD_ROWS):
        row = []
        for col in range(consts.BOARD_COLS):
            row.append("EMPTY")
        board.append(row)
    return board

def Loading_assets():
    soldier_image = pygame.image.load(consts.SOLDIER_IMG)
    soldier_resized = pygame.transform.scale(
        soldier_image, (consts.SOLDIER_BODY_WIDTH, consts.SOLDIER_BODY_HEIGHT))

    flag_image = pygame.image.load("flag.png")
    flag_resized = pygame.transform.scale(
        flag_image, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))

    grass_image = pygame.image.load("grass.png")
    grass_resized = pygame.transform.scale(
        grass_image, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))

    return soldier_resized, flag_resized, grass_resized
def create_mines():
    mine_positions = []
    x = consts.MINE_NUMBER
    for i in range(x):
        mine_x = random.choice(range(consts.BOARD_COLS))
        mine_y = random.choice(range(consts.BOARD_ROWS))
        mine_positions.append((mine_x, mine_y))
    return mine_positions

def append_mines(board, mine_positions):
    for mine in mine_positions:
        mine_x = mine[0]
        mine_y = mine[1]
        if board[mine_y][mine_x-1]  == "EMPTY" and board[mine_y][mine_x+1] == "EMPTY":
            board[mine_y][mine_x] = board[mine_y][mine_x+1] = board[mine_y][mine_x-1] = "MINE"
        else:
            mine += 1
    return board