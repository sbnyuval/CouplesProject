import pygame
import consts
import Screen
import soldier
import game_field
import random
import sys
def main():
    pygame.init()
    pygame.display.set_caption("The Flag")
    screen, clock = Screen.init_game()
    Screen.welcome_message()
    soldier_resized, flag_resized, grass_resized = game_field.Loading_assets()
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT
    grass_positions = Screen.create_grass()
    player_x = soldier.player_x - 5
    player_y = soldier.player_y
    font = pygame.font.SysFont("Arial", 50, bold=True)
    mines_list = []
    running = True
    won = False
    lost = False
    while running:
        clock.tick(60)
        event_status = Incident_Handling()
        if event_status == "enter":
            mines_list = game_field.create_mines()
            Screen.Screen2(mines_list)
        elif event_status is False:
            running = False
        if not won and not lost:
            player_x, player_y = update_player_position(player_x, player_y)
            player_rect = pygame.Rect(player_x, player_y, consts.SOLDIER_BODY_WIDTH, consts.SOLDIER_BODY_HEIGHT)
            flag_rect = pygame.Rect(flag_x, flag_y, consts.FLAG_WIDTH, consts.FLAG_HEIGHT)
            if player_rect.colliderect(flag_rect):
                won = True
            for mine in mines_list:
                mine_rect = pygame.Rect(mine) if not isinstance(mine, pygame.Rect) else mine
                if player_rect.colliderect(mine_rect):
                    lost = True
        Screen.draw_screen(
            screen, soldier_resized, flag_resized, grass_resized,
            grass_positions, player_x, player_y, flag_x, flag_y
        )
        if won:
            draw_victory_message(screen, font)
        elif lost:
            draw_defeat_message(screen, font)
        pygame.display.flip()
    pygame.quit()
    sys.exit()
def draw_victory_message(screen, font):
    text_surface = font.render("You Won!", True, (0, 255, 0))
    text_rect = text_surface.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))
    bg_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, (0, 0, 0), bg_rect)
    screen.blit(text_surface, text_rect)
def draw_defeat_message(screen, font):
    text_surface = font.render("You lose!", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2))
    bg_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(screen, (0, 0, 0), bg_rect)
    screen.blit(text_surface, text_rect)
def Incident_Handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You pressed a key.Enter!")
                return "enter"
            elif event.key == pygame.K_UP:
                print("You clicked the up arrow!")
            elif event.key == pygame.K_DOWN:
                print("You clicked the down arrow!")
            elif event.key == pygame.K_LEFT:
                print("You pressed the left arrow!")
            elif event.key == pygame.K_RIGHT:
                print("You pressed the right arrow!")
    return True
def update_player_position(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if x < 0:
        x = 0
    elif x > consts.WINDOW_WIDTH - consts.SOLDIER_BODY_WIDTH:
        x = consts.WINDOW_WIDTH - consts.SOLDIER_BODY_WIDTH

    if y < 0:
        y = 0
    elif y > consts.WINDOW_HEIGHT - consts.SOLDIER_BODY_HEIGHT:
        y = consts.WINDOW_HEIGHT - consts.SOLDIER_BODY_HEIGHT
    return x, y
if __name__ == "__main__":
    main()



