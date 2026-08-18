import pygame
import consts
import random
import sys

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()

def get_flag():
    flag_image = pygame.image.load("flag.png")
    flag_resized = pygame.transform.scale(flag_image, (consts.FLAG_WIDTH, consts.FLAG_WIDTH))
    flag_x = (consts.WINDOW_WIDTH - consts.FLAG_WIDTH)
    flag_y = (consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT)
    screen.blit(flag_resized, (flag_x, flag_y))

def create_grass():
    grass_positions = []
    for i in range(20):
        grass_x = random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        grass_y = random.randint(0, consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        grass_positions.append((grass_x, grass_y))
    return grass_positions

def run_screen():
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
    welcome_message()
    pygame.display.flip()

def Screen2(mine_positions, player_x, player_y):
    soldier_night_image = pygame.image.load("soldier_nigth.png")
    soldier_night_resized = pygame.transform.scale(soldier_night_image, (consts.FLAG_WIDTH, consts.FLAG_WIDTH))

    mine_img = pygame.image.load("mine.png")
    mine_resized = pygame.transform.scale(mine_img, (consts.MINE_WIDTH, consts.MINE_HEIGHT))

    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(consts.BLACK)

        for x in range(consts.BOARD_SOLS):
            for y in range(consts.BOARD_ROWS):
                rect = pygame.Rect(x * consts.TILE_SIZE, y * consts.TILE_SIZE, consts.TILE_SIZE, consts.TILE_SIZE)
                pygame.draw.rect(screen, consts.DARK_GREEN, rect, 1)
        screen.blit(soldier_night_resized, (player_x-20, player_y))

        for mine in mine_positions:
            screen.blit(mine_resized, (mine[0] * 20, mine[1] * 20))
        pygame.display.flip()
        clock.tick(60)

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

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def welcome_message():
    draw_message("Welcome to The Flag game. Have Fun!", 20, (255, 255, 255), (20,20))