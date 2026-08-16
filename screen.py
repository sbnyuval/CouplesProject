import pygame
import consts
pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("The Flag")
clock = pygame.time.Clock()
def get_flag():
    flag_image = pygame.image.load("flag.png")
    flag_resized = pygame.transform.scale(flag_image, (consts.FLAG_WIDTH, consts.FLAG_WIDTH))
    flag_x = (consts.WINDOW_WIDTH - consts.FLAG_WIDTH)
    flag_y = (consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT)
    screen.blit(flag_resized, (flag_x, flag_y))


def ran_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("Dark green")
        get_flag()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("Incident Review")
    clock = pygame.time.Clock()
    return screen, clock
def draw_screen(screen, soldier, flag, grass, grass_positions, player_x, player_y, flag_x, flag_y):
    screen.fill(consts.DARK_GREEN)
    for pos in grass_positions:
        screen.blit(grass, pos)
    screen.blit(flag, (flag_x, flag_y))
    screen.blit(soldier, (player_x, player_y))
    pygame.display.flip()

