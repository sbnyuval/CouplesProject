import pygame
import consts
import Screen
import soldier
import game_field
import random
import sys


def main():
    pygame.init()
    empty_board = game_field.create_board()
    mines = game_field.create_mines(empty_board)
    board = game_field.append_mines(empty_board, mines)
    game_field.append_soldier_legs(board)
    game_field.append_soldier_body(board)
    game_field.append_flag(board)
    for row in board:
        print(row)
    pygame.display.set_caption("The Flag")
    screen, clock = Screen.init_game()
    Screen.welcome_message()
    soldier_resized, flag_resized, grass_resized = game_field.Loading_assets()
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT

    grass_positions = Screen.create_grass()

    player_x = soldier.player_x
    player_y = soldier.player_y

    running = True
    while running:
        clock.tick(60)
        game_status, player_x, player_y = Incident_Handling(player_x, player_y)

        if game_status == False:
            running = False
        elif game_status == "enter":
            Screen.Screen2(mines, player_x, player_y)

        player_x = max(0, min(player_x, consts.WINDOW_WIDTH - consts.SOLDIER_BODY_WIDTH))
        player_y = max(0, min(player_y, consts.WINDOW_HEIGHT - consts.SOLDIER_BODY_HEIGHT))
        Screen.draw_screen(
            screen, soldier_resized, flag_resized, grass_resized, grass_positions, player_x - 20, player_y, flag_x, flag_y)

    pygame.quit()
    sys.exit()


def Incident_Handling(x, y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, x, y

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You pressed a key.Enter!")
                return "enter", x, y
            elif event.key == pygame.K_UP:
                print("You clicked the up arrow!")
                y -= 20
            elif event.key == pygame.K_DOWN:
                print("You clicked the down arrow!")
                y += 20
            elif event.key == pygame.K_LEFT:
                print("You pressed the left arrow!")
                x -= 20
            elif event.key == pygame.K_RIGHT:
                print("You pressed the right arrow!")
                x += 20

    return True, x, y

def is_won(board):
    for row in range(22, 25):
        for col in range(46, 50):
            board[row][col] = "SOLDIER_BODY"
    return True

def is_lost(board):
    pass

if __name__ == "__main__":
    main()
