from colors import YELLOW
from pathSegment import PathSegment


class Path:
    def __init__(self, segmentLocations, width, color = YELLOW):
        self.pathSegmentList = []
        for i in segmentLocations:
            self.pathSegmentList.append(PathSegment(i[0], i[1], width, color))

    def render(self, screen):
        for i in range(len(self.pathSegmentList)):
            PathSegment.render(self.pathSegmentList[i], screen)

    def getStartIndex(self):
        return 0

    def getStartCoordinate(self):
        return self.pathSegmentList[0].getCenter()

    def getSegmentCoordinates(self, pathIndex):
        return self.pathSegmentList[pathIndex + 1].getCenter()

    def updateIndex(self, pathIndex):
        return pathIndex + 1

    def reachedEnd(self, pathIndex):
        if pathIndex == len(self.pathSegmentList) - 1:
            return True
        return False

