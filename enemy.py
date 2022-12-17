from path import Path

class Slime:
    def __init__(self, speed, health, followedpath: Path):
        self.health = health
        self.speed = speed
        self.followedpath = followedpath
        self.pathIndex = followedpath.getStartIndex()
        self.x = self.followedpath.getStartCoordinate()[0]
        self.y = self.followedpath.getStartCoordinate()[1]

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
        target = self.followedpath.getSegmentCoordinates(self.pathIndex)
        dir = self.direction(target)
        if abs((self.x - target[0]) + (self.y - target[1])) >= self.speed:
            if dir == 1:
                self.x -= self.speed
            elif dir == 2:
                self.x += self.speed
            elif dir == 3:
                self.y -= self.speed
            else:
                self.y += self.speed

        else:
            overshoot =  self.speed - abs((self.x - target[0]) + (self.y - target[1]))
            if dir == 1:
                self.x -= self.speed - overshoot
            elif dir == 2:
                self.x += self.speed - overshoot
            elif dir == 3:
                self.y -= self.speed - overshoot
            else:
                self.y += self.speed - overshoot

        if abs((self.x - target[0]) + (self.y - target[1])) == 0:
            self.pathIndex = self.followedpath.updateIndex(self.pathIndex)

            #go back to start until no speed left



