

class Slime:
    def __init__(self, speed, health, followedpath):
        self.health = health
        self.speed = speed
        self.followedpath = followedpath
        self.pathIndex = followedpath.getStart()

    def update(self):
        target = self.followedpath.getSegmentCoordinates(self.pathIndex)

