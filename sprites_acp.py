import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle Movement")
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 60, 60)
clock = pygame.time.Clock()
rect1_width = 60
rect1_height = 60
rect1_x = 100
rect1_y = 100
rect1_speed = 5
rect2 = pygame.Rect(500, 250, 80, 80)
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= rect1_speed
    if keys[pygame.K_RIGHT]:
        player_x += rect1_speed
    if keys[pygame.K_UP]:
        player_y -= rect1_speed
    if keys[pygame.K_DOWN]:
        player_y += rect1_speed
    player_x = max(0, min(WIDTH - rect1_width, player_x))
    player_y = max(0, min(HEIGHT - rect1_height, player_y))
    player_rect = pygame.Rect(player_x, player_y, rect1_width, rect1_height)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, rect2)
    pygame.display.flip()
pygame.quit()
sys.exit()