"""
Given an array of positive integers nums and a positive integer target, return the minimal length
 of a subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        start = 0
        end = 0
        _sum = 0
        _count = float('inf')
        while end < len(nums):
            _sum += nums[end]
            while _sum >= target:
                length = end - start + 1
                _count = min(_count, length)
                _sum -= nums[start]
                start += 1
            end += 1
        return _count if _count != float('inf') else 0


if __name__ == '__main__':
    result = Solution().minSubArrayLen(11, [1, 2, 3, 4, 5])
    assert result == 3
