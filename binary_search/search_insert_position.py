from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = -1
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return mid + 1


if __name__ == '__main__':
    Solution().searchInsert([1, 3, 5, 6], 5)
