from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """

        :param nums:
        :param val:
        :return:
        """
        if not nums:
            return 0

        array_index = 0
        new_index = 0
        length = len(nums)
        while array_index < length:
            if nums[array_index] != val:
                nums[new_index] = nums[array_index]
                new_index += 1
            array_index += 1
        return new_index


class TestSolution:

    def test_remove_elem_01(self):
        nums = [3, 2, 2, 3, 2]
        val = 3
        non_elements = 3
        result = Solution().removeElement(nums, val)
        assert result == non_elements
