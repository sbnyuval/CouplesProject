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
        old_x, old_y = player_x, player_y

        game_status, player_x, player_y = Incident_Handling(player_x, player_y)

        if game_status == False:
            running = False
        elif game_status == "enter":
            Screen.Screen2(mines, player_x, player_y)

        player_x = max(0, min(player_x, consts.WINDOW_WIDTH - consts.SOLDIER_BODY_WIDTH))
        player_y = max(0, min(player_y, consts.WINDOW_HEIGHT - consts.SOLDIER_BODY_HEIGHT))
        if old_x != player_x or old_y != player_y:
            update_soldier_in_matrix(board, old_x, old_y, player_x, player_y)
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


def update_soldier_in_matrix(board, old_x, old_y, new_x, new_y):

    CELL_SIZE = 20

    old_start_row = old_y // CELL_SIZE
    old_start_col = old_x // CELL_SIZE

    # נניח שהגוף והרגליים תופסים שטח מסוים (למשל 3 שורות על 2 עמודות - יש להתאים למשחק שלך)
    # ננקה ריבוע זמני מסביב למיקום הישן
    for r in range(old_start_row, old_start_row + 4):
        for c in range(old_start_col, old_start_col + 2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                # מנקים רק את חלקי החייל, לא דורסים מוקשים או דגל!
                if board[r][c] in ["SOLDIER_BODY", "SOLDIER_LEGS"]:
                    board[r][c] = "EMPTY"

    # 2. השמת המיקום החדש במטריצה
    new_start_row = new_y // CELL_SIZE
    new_start_col = new_x // CELL_SIZE

    # השמת גוף החייל (למשל 3 השורות הראשונות)
    for r in range(new_start_row, new_start_row + 3):
        for c in range(new_start_col, new_start_col + 2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                board[r][c] = "SOLDIER_BODY"

    # השמת רגלי החייל (השורה הרביעית מתחת לגוף)
    legs_row = new_start_row + 3
    for c in range(new_start_col, new_start_col + 2):
        if 0 <= legs_row < len(board) and 0 <= c < len(board[0]):
            board[legs_row][c] = "SOLDIER_LEGS"


def is_won(board):
    for row in range(22, 25):
        for col in range(46, 50):
            board[row][col] = "SOLDIER_BODY"
    return True

def is_lost(board):
    pass

if __name__ == "__main__":
    main()
