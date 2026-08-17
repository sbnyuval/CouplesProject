import pygame
import consts
import Screen
import soldier
import game_field
import random
import sys


def main():
    pygame.init()
    board = game_field.create()
    pygame.display.set_caption("The Flag")
    screen, clock = Screen.init_game()
    Screen.welcome_message()
    soldier_resized, flag_resized, grass_resized = game_field.Loading_assets()
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT
    grass_positions = Screen.create_grass()
    running = True
    while running:
        clock.tick(60)
        running = Incident_Handling()
        player_x, player_y = update_player_position(soldier.player_x, soldier.player_y)
        Screen.draw_screen(
            screen, soldier_resized, flag_resized, grass_resized, grass_positions, player_x, player_y, flag_x, flag_y)
    pygame.quit()
    sys.exit()
def Incident_Handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("You pressed a key.Enter!")
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