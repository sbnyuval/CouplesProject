import random

import pygame
import consts
import Screen
board = []
mine_positions = []
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
def create_mines(board):
    for i in range(consts.MINE_NUMBER):
        mine_x = random.choice(range(consts.BOARD_COLS-2))
        mine_y = random.choice(range(consts.BOARD_ROWS))
        if board[mine_y][mine_x]  == "MINE" or board[mine_y][mine_x-2]  == "MINE" or board[mine_y][mine_x+2] == "MINE" or board[mine_y][mine_x] == "SOLDIER_LEGS" or board[mine_y][mine_x] == "SOLDIER_BODY" or mine_x == 0:
            i += 1
        else:
            board[mine_y][mine_x] = board[mine_y][mine_x+1] = board[mine_y][mine_x-1] = "MINE"
        mine_positions.append([mine_x, mine_y])
    return mine_positions

def create_mines_tuple():
    mine_positions_tuple = []
    for mine in mine_positions:
        mine_x = mine_positions[mine][0]
        mine_y = mine_positions[mine][1]
        mine_positions_tuple.append((mine_x, mine_y))
    return mine_positions_tuple


def append_mines(board, mine_positions):
    for mine in mine_positions:
        mine_x = mine[0]
        mine_y = mine[1]
        board[mine_y][mine_x] = board[mine_y][mine_x+1] = board[mine_y][mine_x-1] = "MINE"
    return board

def append_soldier_legs(board):
    for row in range(3, 4):
        for col in range(2):
            board[row][col] = "SOLDIER_LEGS"
    return board

def append_soldier_body(board):
    for row in range(0, 3):
        for col in range(2):
            board[row][col] = "SOLDIER_BODY"
    return board

def append_flag(board):
    for row in range(22, 25):
        for col in range(46, 50):
            board[row][col] = "FLAG"
    return board

def clear_soldier(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in ["SOLDIER_BODY", "SOLDIER_LEGS"]:
                board[row][col] = "EMPTY" 
