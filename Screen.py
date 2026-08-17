import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
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
    pygame.display.set_caption("Incident Review")
    return screen, clock
def draw_screen(screen, soldier, flag, grass, grass_positions, player_x, player_y, flag_x, flag_y):
    screen.fill(consts.DARK_GREEN)
    for pos in grass_positions:
        screen.blit(grass, pos)
    screen.blit(flag, (flag_x, flag_y))
    screen.blit(soldier, (player_x, player_y))
    pygame.display.flip()
def Screen2 ():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and consts.player_x > 0:
                    consts.player_x -= 1
                if event.key == pygame.K_RIGHT and consts.player_x < consts.BOARD_SOLS - 1:
                    consts.player_x += 1
                if event.key == pygame.K_UP and consts.player_y > 0:
                    consts.player_y -= 1
                if event.key == pygame.K_DOWN and consts.player_y < consts.BOARD_ROWS - 1:
                    consts.player_y += 1

        screen.fill(consts.BLACK)
        for x in range(consts.BOARD_SOLS):
            for y in range(consts.BOARD_ROWS):
                rect = pygame.Rect(x * consts.TILE_SIZE, y * consts.TILE_SIZE, consts.TILE_SIZE, consts.TILE_SIZE)
                pygame.draw.rect(screen, consts.DARK_GREEN, rect, 1)

        player_rect = pygame.Rect(consts.player_x * consts.TILE_SIZE, consts.player_y * consts.TILE_SIZE, consts.TILE_SIZE, consts.TILE_SIZE)
        pygame.draw.rect(screen, consts.red, player_rect)
        pygame.display.flip()
        clock.tick(60)
Screen2()


