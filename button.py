import pygame
from colors import BLACK, WHITE
class TowerButton:
    def __init__(self, towerName, Tower, x, y, width, height, color):
        self.towerName = towerName
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rectangle = pygame.Rect(x - (1 / 2 * self.width), y - (1 / 2 * self.height), width, height)
        #Tower is class
        self.towerWidth = 50
        self.tower = Tower(0, 0, self.towerWidth, 0, x, y, splash = 0, neutral = True, placing = False)


    def render(self, screen):
        font = pygame.font.SysFont("Arial", 10)
        fontSurface = font.render(self.towerName, True, WHITE)
        pygame.draw.rect(screen, self.color, (self.x - (1 / 2 * self.width), self.y - (1 / 2 * self.height), self.width, self.height))
        self.tower.render(screen, None, "")
        screen.blit(fontSurface, (self.x - (1/2 * fontSurface.get_width()), self.y + (1/2 * self.towerWidth)))

    def isClicked(self, x, y):
        return self.rectangle.collidepoint(x, y)
