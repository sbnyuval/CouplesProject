import pygame
import consts
# import screen
import soldier
import game_field
pygame.init()

clock = pygame.time.Clock()
soldier_image = pygame.image.load(consts.SOLDIER_IMG)
soldier_resized = pygame.transform.scale(soldier_image, (consts.SOLDIER_BODY_WIDTH, consts.SOLDIER_BODY_HEIGHT))
player_x = 0
player_y = 0
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
    screen.fill(consts.DARK_GREEN)
    screen.blit(soldier_resized, (player_x, player_y))
    pygame.display.flip()
pygame.quit()


