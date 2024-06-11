from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        start, end = newInterval
        for interval in intervals:
            if interval[1] < start:
                result.append(interval)
                continue
            if interval[0] > end:
                result.append([start, end])
                start, end = interval
                continue
            start = min(interval[0], start)
            end = max(interval[1], end)
        result.append([start, end])
        return result


if __name__ == '__main__':
    result = Solution().insert([[1, 3], [6, 9]], [2, 5])
    assert result == [[1, 5], [6, 9]]
