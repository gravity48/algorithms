from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        def rec(k, mas):
            if len(mas) == 1:
                return k
            for index, item in enumerate(mas):
                if item + index >= len(mas) - 1:
                    return rec(k + 1, mas[:index + 1])

        count = rec(0, nums)
        return count


if __name__ == '__main__':
    Solution().jump([2, 3, 1, 1, 4])
