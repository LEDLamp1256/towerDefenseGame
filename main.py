import pygame
COLORWHITE = (255, 255, 255)

pygame.init()

SCREENX = 400
SCREENY = 400
screen = pygame.display.set_mode((SCREENX, SCREENY))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(COLORWHITE)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 200), width=1)

    pygame.display.update()
pygame.quit()
