from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        _prev = nums[0]
        count = 0
        for num in nums[1:]:
            if _prev >= num:
                count += _prev - num + 1
                _prev += 1
            else:
                _prev = num
        return count

if __name__ == '__main__':
    res = Solution().minIncrementForUnique([1,2,2])
    print(res)