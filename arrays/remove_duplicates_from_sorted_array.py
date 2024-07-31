from typing import List
from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        replace_index = 0
        hashes = defaultdict(lambda: 0)
        for index in range(len(nums)):
            value = nums[index]
            hashes[value] += 1
            count = hashes[value]
            if count > 2:
                continue
            nums[replace_index] = nums[index]
            replace_index += 1
        return replace_index


class NewSolution:

    def removeDublicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        index0 = 0
        index1 = 1
        k = 0
        while index1 < len(nums):
            if nums[index0] == nums[index1] and k > 0:
                ...
            elif nums[index0] == nums[index1]:
                k += 1
                index0 += 1
                nums[index0] = nums[index1]
            elif nums[index0] != nums[index1]:
                k = 0
                index0 += 1
                nums[index0] = nums[index1]
            index1 += 1
        return index0 + 1


class TestRemoveDuplicatesFromArray:

    def test_remove_duplicates_from_array_01(self):
        nums = [1, 1, 1, 2, 2, 3]
        Solution().removeDuplicates(nums)
        assert nums == [1, 1, 2, 2, 3, 3]

    def test_new_remove_duplicates_from_array_02(self):
        nums = [1, 1, 1, 2, 2, 3]
        NewSolution().removeDublicates(nums)
        assert nums == [1, 1, 2, 2, 3, 3]