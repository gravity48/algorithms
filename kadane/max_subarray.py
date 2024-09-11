from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_sum = 0
        global_sum = float('-inf')

        for num in nums:
            local_sum = max(num, local_sum + num)
            global_sum = max(local_sum, global_sum)

        return global_sum


if __name__ == '__main__':
    Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
