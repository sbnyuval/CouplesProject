
import pygame
import consts
import random
import sys

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("Incident Review")
    clock = pygame.time.Clock()
    return screen, clock
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
    return x, y
def draw_screen(screen, soldier, flag, grass, grass_positions, player_x, player_y, flag_x, flag_y):
    screen.fill(consts.DARK_GREEN)
    for pos in grass_positions:
        screen.blit(grass, pos)
    screen.blit(flag, (flag_x, flag_y))
    screen.blit(soldier, (player_x, player_y))
    pygame.display.flip()
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

