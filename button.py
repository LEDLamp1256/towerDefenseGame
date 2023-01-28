import pygame

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
        self.tower = Tower(0, 0, 10, 0, x, y, splash = 0, neutral = True, placing = False)


    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - (1 / 2 * self.width), self.y - (1 / 2 * self.height), self.width, self.height))
        self.tower.render(screen, None, "")

    def ifClicked(self, x, y):
        self.rectangle.collidepoint(x, y)