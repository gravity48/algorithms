from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        if len(points) == 1:
            return 1
        result = []
        start, end = sorted_points[0]
        for interval in sorted_points[1:]:
            if end < interval[0]:
                result.append([start, end])
                start, end = interval
                continue
            start = max(interval[0], start)
            end = min(interval[1], end)
        result.append([start, end])
        return len(result)


if __name__ == '__main__':
    Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
