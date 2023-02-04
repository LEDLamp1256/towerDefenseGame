import time
from colors import WHITE, BLACK,  GREEN
import pygame
from path import Path
from enemy import Slime
from player import Player
from button import TowerButton
from tower import ArrowTower
pygame.init()

#

SCREENX = 800
SCREENY = 800
screen = pygame.display.set_mode((SCREENX, SCREENY))
gamePath = Path([(0,0),(50, 0), (50, 50), (100, 50), (100,0)], 40, BLACK)
testSlime = Slime(0.1, 10, gamePath, GREEN, 5, 11)
testPlayer = Player(10, 1000)

test = 0
clock = pygame.time.Clock()
frameRateTest = time.time()

testButton = TowerButton("ArrowTower", ArrowTower, 50, 750, 100, 100, BLACK)

enemyList = [testSlime]
towerList = []
placingTower = None

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if testButton.isClicked(event.pos[0], event.pos[1]):
                    print("Click")
                    placingTower = ArrowTower(1, 1, 50, 100, event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEMOTION:
            if placingTower:
                placingTower.positionUpdate(event.pos[0], event.pos[1])

    screen.fill(WHITE)

    testButton.render(screen)
    if placingTower:
        placingTower.render(screen, gamePath, towerList)
    gamePath.render(screen)

    finishedEnemyList = []
    for i in range(len(enemyList)):
        if enemyList[i].update():
            finishedEnemyList.append(enemyList[i])
            testPlayer.health -= testSlime.damage
        enemyList[i].render(screen)
    for i in range(len(finishedEnemyList)):
        enemyList.remove(finishedEnemyList[i])

    pygame.display.update()
    if testPlayer.health <= 0:
        done = True
    clock.tick(60)
pygame.quit()





# pygame.draw.rect(screen, (0, 0, 0), (0 + test, 0, 100, 200), width=0)
    # test += 1
    # if test == 300:
    #     duration =  time.time() - frameRateTest
    #     print(300 /duration)
