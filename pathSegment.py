import pygame
from colors import YELLOW


class PathSegment:
    def __init__(self, x, y, width, color = YELLOW):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.center = (x + width/2, y + width/2)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), width=0)

    def getCenter(self):
        return self.center