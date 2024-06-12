"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j,
i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        triplets = set()
        nums.sort()
        for i in range(len(nums) - 2):
            k = len(nums) - 1
            j = i + 1
            while k > j:
                _sum = nums[k] + nums[j] + nums[i]
                if _sum == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    k -= 1
                if _sum < 0:
                    j += 1
                if _sum > 0:
                    k -= 1
        return triplets


if __name__ == '__main__':
    Solution().threeSum([-1, 0, 1, 2, -1, -4])
