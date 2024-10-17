class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        points.sort(key=lambda x: x[1])
        arrows, end = 1, points[0][1]
        for point in points:
            if point[0] > end:
                arrows += 1
                end = point[1]
        return arrows