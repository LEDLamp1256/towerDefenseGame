import pygame
from colors import GREEN, RED, SILVER

class ArrowTower:
    cost = 400
    def __init__(self, damage, attackSpeed, width, range, x, y, splash = 0, neutral = False, placing = True):
        self.damage = damage
        self.attackSpeed = attackSpeed
        self.width = width
        self.range = range
        self.x = x
        self.y = y
        self.splash = splash
        self.placing = placing
        self.neutral = neutral
        self.rectangle = pygame.Rect(self.x - (1/2 * self.width), self.y - (1/2 * self.width), self.width, self.width   )


    def render(self, screen, path, towers):
        if self.placing and not self.buildingCollisionCheck(path, towers):
            pygame.draw.rect(screen, GREEN, (self.x - (1/2 * self.width), self.y - (1/2 * self.width), self.width, self.width))
            pygame.draw.circle(screen, RED, (self.x, self.y), self.range, 3)
        elif self.placing and self.buildingCollisionCheck(path, towers):
            pygame.draw.rect(screen, RED, (self.x - (1/2 * self.width), self.y - (1/2 * self.width), self.width, self.width))
            pygame.draw.circle(screen, RED, (self.x, self.y), self.range, 3)
        elif not self.placing:
            pygame.draw.rect(screen, SILVER, (self.x - (1/2 * self.width), self.y - (1/2 * self.width), self.width, self.width))


    def attack(self, path):
        if not self.neutral:
            pass
        pass

    def positionUpdate(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(self.x - (1/2 * self.width), self.y - (1/2 * self.width), self.width, self.width)

    def setBuilding(self, path, towers):
        #part of code where building is placed/set
        #check if self.placing, and set it to false after
        if self.placing and not self.buildingCollisionCheck(path, towers):
            self.placing = False
            return True
        else:
            return False


    def buildingCollisionCheck(self, path, towers):
        collisionRects = []
        for i in towers:
            collisionRects.append(i.rectangle)
        collisionRects.extend(path.getRectangles())
        if self.rectangle.collidelist(collisionRects) == -1:
            #if not colliding case
            return False
        else:
            #if colliding case
            return True

