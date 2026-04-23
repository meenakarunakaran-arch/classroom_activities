import pygame
pygame.init()

# window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

# background color
bg_color = (58, 58, 58)

# load image (put your image file in same folder)
img = pygame.image.load("image.png")
img = pygame.transform.scale(img, (300, 300))

# get center position
rect = img.get_rect(center=(250, 250))

# game loop
running = True
while running:
    screen.fill(bg_color)
    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()