import pygame

pygame.init()

# window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

# colors
white = (255, 255, 255)
blue = (0, 0, 255)

# font
font = pygame.font.SysFont(None, 40)
text = font.render("Hello Dakshita!", True, (0, 0, 0))

# rectangle (center)
rect = pygame.Rect(0, 0, 150, 100)
rect.center = (320, 240)

# loop
running = True
while running:
    screen.fill(white)

    # draw rectangle
    pygame.draw.rect(screen, blue, rect)

    # show text
    screen.blit(text, (200, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()