import collections
from typing import List


class Solution:
    def findSlope(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 - x2 == 0:
            return float('inf')
        return (y1 - y2)/(x1 - x2)

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        ans = 1
        for index, point1 in enumerate(points):
            slopes = collections.defaultdict(int)
            for index2, point2 in enumerate(points[index + 1:]):
                slope = self.findSlope(point1, point2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1
