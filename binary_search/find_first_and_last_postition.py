from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) < 2:
            return [0, 0] if nums[0] == target else [-1, -1]
        length = len(nums)
        left = 0
        right = length - 1
        is_find = False
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                right = mid - 1
                is_find = True
            elif mid + 1 < length and nums[mid] == nums[mid + 1]:
                right = mid
                is_find = True
            else:
                is_find = True
                right = mid
        if nums[right] == target:
            is_find = True
        if not is_find:
            return [-1,-1]
        start = right
        end = start
        while end < length and nums[end] == target:
            end += 1
        return [start, end - 1]
