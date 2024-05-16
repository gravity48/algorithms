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


class TestRemoveDuplicatesFromArray:

    def test_remove_duplicates_from_array_01(self):
        nums = [1, 1, 1, 2, 2, 3]
        Solution().removeDuplicates(nums)
        assert nums == [1, 1, 2, 2, 3, 3]
