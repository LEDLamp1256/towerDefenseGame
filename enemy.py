from path import Path
import pygame
class Slime:
    def __init__(self, speed, health, followedpath: Path, color, radius, damage):
        self.health = health
        self.speed = speed
        self.followedpath = followedpath
        self.pathIndex = followedpath.getStartIndex()
        self.x = self.followedpath.getStartCoordinate()[0]
        self.y = self.followedpath.getStartCoordinate()[1]
        self.color = color
        self.radius = radius
        self.damage = damage

    # 1 is left, 2 is right, 3 is up, 4 is down
    def direction(self, targetxy):
        selfxy = (self.x, self.y)
        if selfxy[0] == targetxy[0]:
            if selfxy[1] > targetxy[1]:
                return 3
            else:
                return 4
        if selfxy[0] > targetxy[0]:
            return 1
        else:
            return 2

    def update(self):
        if self.followedpath.reachedEnd(self.pathIndex):
            return True
        remainingSpeed = self.speed
        while remainingSpeed > 0:
            target = self.followedpath.getSegmentCoordinates(self.pathIndex)
            dir = self.direction(target)
            if abs((self.x - target[0]) + (self.y - target[1])) >= remainingSpeed:
                if dir == 1:
                    self.x -= remainingSpeed
                elif dir == 2:
                    self.x += remainingSpeed
                elif dir == 3:
                    self.y -= remainingSpeed
                else:
                    self.y += remainingSpeed
                remainingSpeed = 0
            else:
                overshoot =  remainingSpeed - abs((self.x - target[0]) + (self.y - target[1]))
                if dir == 1:
                    self.x -= remainingSpeed - overshoot
                elif dir == 2:
                    self.x += remainingSpeed - overshoot
                elif dir == 3:
                    self.y -= remainingSpeed - overshoot
                else:
                    self.y += remainingSpeed - overshoot
                remainingSpeed = overshoot

            if abs((self.x - target[0]) + (self.y - target[1])) == 0:
                self.pathIndex = self.followedpath.updateIndex(self.pathIndex)
                if self.followedpath.reachedEnd(self.pathIndex):
                    return True
        return False

                #go back to start until no speed left

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)



