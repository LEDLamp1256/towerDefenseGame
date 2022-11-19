from colors import YELLOW
from pathSegment import PathSegment


class Path:
    def __init__(self, segmentLocations, width, color = YELLOW):
        self.pathSegmentList = []
        for i in segmentLocations:
            self.pathSegmentList.append(PathSegment(i[0], i[1], width, color))


