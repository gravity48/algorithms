from typing import List
import collections


class MySolution:
    def binarySearch(self, target, up=False):
        left = 0
        right = len(self._sorted_list) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self._sorted_list[mid] == target:
                if up:
                    return mid + 1, mid + 1
                return mid, mid
            elif self._sorted_list[mid] > target:
                right = mid - 1
            elif self._sorted_list[mid] < target:
                left = mid + 1
        return left, right


    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        _map = collections.defaultdict(lambda: [])
        self._sorted_list = sorted(list(set(nums)))
        _results = set()
        for index, num in enumerate(nums):
            _map[num].append(index)
        for index, num in enumerate(nums):
            start, _ = self.binarySearch(lower - num)
            stop, _ = self.binarySearch(upper - num, True)
            for item in self._sorted_list[start: stop]:
                for index1 in _map[item]:
                    if (
                        index1 != index
                        and (index1, index) not in _results
                        and (index, index1) not in _results
                    ):
                        _results.add((index, index1))
        return len(_results)


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)

    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1

        return count


if __name__ == '__main__':
    Solution().countFairPairs([0,1,7,4,4,5],3, 6 )

