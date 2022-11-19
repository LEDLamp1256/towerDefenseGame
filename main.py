import time
from colors import WHITE
import pygame


pygame.init()

SCREENX = 400
SCREENY = 400
screen = pygame.display.set_mode((SCREENX, SCREENY))


test = 0
clock = pygame.time.Clock()
frameRateTest = time.time()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    pygame.draw.rect(screen, (0, 0, 0), (0 + test, 0, 100, 200), width=0)
    test += 1
    if test == 300:
        duration =  time.time() - frameRateTest
        print(300 /duration)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
