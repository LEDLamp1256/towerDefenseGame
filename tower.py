import pygame
from colors import GREEN, RED, SILVER

class ArrowTower:
    cost = 400
    def __init__(self, damage, attackSpeed, width, range, x, y, splash = 0):
        self.damage = damage
        self.attackSpeed = attackSpeed
        self.width = width
        self.range = range
        self.x = x
        self.y = y
        self.splash = splash
        self.placing = True
        self.rectangle = pygame.Rect(x, y, width, width)

    def render(self, screen, path, towers):
        if self.placing and not self.buildingCollisionCheck(path, towers):
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.width))
        elif self.placing and self.buildingCollisionCheck(path, towers):
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.width))
        elif not self.placing:
            pygame.draw.rect(screen, SILVER, (self.x, self.y, self.width, self.width))

    def attack(self, path):
        pass

    def positionUpdate(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x, y, self.width, self.width)
    def setBuilding(self, path, towers):
        pass

    def buildingCollisionCheck(self, path, towers):
        towerRectangles = []
        for i in towers:
            towerRectangles.append(i.rectangle)
        towerRectangles.extend(path.getRectangles())
        if self.rectangle.collidelist(towerRectangles) == -1:
            False

