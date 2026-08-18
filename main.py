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
    font = pygame.font.SysFont("Arial", 50, bold=True)

    game_field.append_soldier_legs(board)
    game_field.append_soldier_body(board)
    game_field.append_flag(board)

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
    game_won = False
    game_lost = False

    while running:
        clock.tick(60)
        old_x, old_y = player_x, player_y
        Screen.welcome_message()

        if not game_won:
            game_status, player_x, player_y = Incident_Handling(player_x, player_y)
            if game_status == False:
                running = False
            elif game_status == "enter":
                Screen.Screen2(mines, player_x, player_y)

            player_x = max(0, min(player_x, consts.WINDOW_WIDTH - consts.SOLDIER_BODY_WIDTH + 40))
            player_y = max(0, min(player_y, consts.WINDOW_HEIGHT - consts.SOLDIER_BODY_HEIGHT))

            if old_x != player_x or old_y != player_y:
                update_soldier_in_matrix(board, old_x, old_y, player_x, player_y)

            if is_lost(player_x, player_y, mines):
                game_lost = True
            elif is_won(board):
                game_won = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        Screen.draw_screen(screen, soldier_resized, flag_resized, grass_resized, grass_positions, player_x - 20, player_y, flag_x, flag_y)

        if game_won:
            draw_victory_message(screen, font)
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False
        elif game_lost:
            draw_defeat_message(screen, font)
            pygame.display.flip() # מעדכן את המסך כדי שהשחקן יראה את הטקסט האדום
            pygame.time.delay(3000) # משהה ל-3 שניות
            running = False
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

    for row in range(old_start_row, old_start_row + 4):
        for col in range(old_start_col, old_start_col + 2):
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] in ["SOLDIER_BODY", "SOLDIER_LEGS"]:
                    board[row][col] = "EMPTY"

    new_start_row = new_y // CELL_SIZE
    new_start_col = new_x // CELL_SIZE

    for row in range(new_start_row, new_start_row + 3):
        for c in range(new_start_col, new_start_col + 2):
            if 0 <= row < len(board) and 0 <= c < len(board[0]):
                board[row][col] = "SOLDIER_BODY"
    legs_row = new_start_row + 3
    for col in range(new_start_col, new_start_col + 2):
        if 0 <= legs_row < len(board) and 0 <= col < len(board[0]):
            board[legs_row][col] = "SOLDIER_LEGS"

def draw_victory_message(screen, font):
    text_surface = font.render("You Won!", True, (0, 255, 0))
    text_rect = text_surface.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))
    bg_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, (0, 0, 0), bg_rect)
    screen.blit(text_surface, text_rect)

def draw_defeat_message(screen, font):
    text_surface = font.render("You Lost!", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))
    bg_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, (0, 0, 0), bg_rect)
    screen.blit(text_surface, text_rect)

def is_won(board):
    for row in range(22, 25):
        for col in range(46, 50):
            if board[row][col] == "SOLDIER_BODY":
                return True
    return False


def is_lost(player_x, player_y, mines):
    CELL_SIZE = 20
    legs_row = (player_y // CELL_SIZE) + 3
    start_col = player_x // CELL_SIZE
    soldier_legs_cols = [start_col, start_col + 1]

    for mine in mines:
        mine_col = mine[0]
        mine_row = mine[1]
        if legs_row == mine_row:
            mine_occupied_cols = [mine_col - 1, mine_col, mine_col + 1]
            for leg_col in soldier_legs_cols:
                if leg_col in mine_occupied_cols:
                    print(f"Boom! Stepped on mine at row {mine_row}, col {mine_col}")
                    return True
    return False


if __name__ == "__main__":
    main()
