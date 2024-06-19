from typing import List


class Solution:
    def find(self, day):
        _count = 0
        neightbours = 0
        for bloom_day in self.bloomDay:
            if bloom_day <= day:
                neightbours += 1
                if neightbours == self.k:
                    _count += 1
                    neightbours = 0
            else:
                neightbours = 0
        return _count >= self.m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        self.m = m
        self.bloomDay = bloomDay
        self.k = k
        l, r = min(bloomDay) - 1, max(bloomDay) + 1
        _result = -1
        while l < r:
            day = l + (r - l) // 2
            if self.find(day):
                _result = day
                r = day
            else:
                l = day + 1
        return _result


if __name__ == '__main__':
    Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3)
