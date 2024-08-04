from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        length = len(ratings)
        candyes = [1] * length
        index = 1
        while index < length:
            if ratings[index] - ratings[index - 1] > 0:
                candyes[index] = candyes[index - 1] + 1
            index += 1
        index = length - 2
        while index > -1:
            if ratings[index] - ratings[index + 1] > 0:
                candyes[index] = max(candyes[index], candyes[index + 1] + 1)
            index -= 1
        return sum(candyes)


if __name__ == '__main__':
    assert Solution().candy([1, 2, 2]) == 4
