import time
from colors import WHITE, BLACK,  GREEN
import pygame
from path import Path
from enemy import Slime
pygame.init()

SCREENX = 400
SCREENY = 400
screen = pygame.display.set_mode((SCREENX, SCREENY))
gamePath = Path([(0,0),(50, 0), (50, 50), (100, 50), (100,0)], 40, BLACK)
testSlime = Slime(0.1, 10, gamePath, GREEN, 5)

test = 0
clock = pygame.time.Clock()
frameRateTest = time.time()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)


    gamePath.render(screen)

    testSlime.update()
    testSlime.render(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()





# pygame.draw.rect(screen, (0, 0, 0), (0 + test, 0, 100, 200), width=0)
    # test += 1
    # if test == 300:
    #     duration =  time.time() - frameRateTest
    #     print(300 /duration)
