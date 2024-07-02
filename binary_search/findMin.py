from typing import List

"""
[4,5,6,7,0,1,2]
[11, 13, 15, 17]
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, lenght = 0, len(nums) - 1, len(nums)
        while r > l:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


if __name__ == '__main__':
    Solution().findMin([2, 3, 4, 5, 1])
