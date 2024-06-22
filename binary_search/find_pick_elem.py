from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r > l:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    Solution().findPeakElement([1, 2, 3, 1])
