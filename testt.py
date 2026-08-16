
import pygame
import consts
import random
import sys
def main():
    screen, clock = init_game()
    soldier_resized, flag_resized, grass_resized = Loading_assets()
    player_x, player_y = 0, 0
    flag_x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT
    grass_positions = []
    for i in range(20):
        rand_x = random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        rand_y = random.randint(0, consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        grass_positions.append((rand_x, rand_y))
    running = True
    while running:
        clock.tick(60)
        running = Incident_Handling()
        player_x, player_y = update_player_position(player_x, player_y)
        draw_screen(
            screen, soldier_resized, flag_resized, grass_resized, grass_positions, player_x, player_y, flag_x, flag_y
        )
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()

