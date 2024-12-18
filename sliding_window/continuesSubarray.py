from collections import deque
from typing import List


class MySolution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total_count = 0
        start = 0
        length = len(nums)
        end = 0
        win = []
        while end < length:
            win.append(nums[end])
            win.sort()
            end += 1
            while (win[-1] - win[0]) > 2:
                win.pop(win.index(nums[start]))
                start += 1
            total_count += len(win)
        return total_count


class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        total_count = 0
        start = 0
        length = len(nums)
        end = 0
        minD, maxD = deque(), deque()
        while end < length:
            while minD and nums[end] <= nums[minD[-1]]: minD.pop()
            while maxD and nums[end] >= nums[maxD[-1]]: maxD.pop()
            minD.append(end)
            maxD.append(end)
            while (nums[maxD[0]] - nums[minD[0]]) > 2:
                start += 1
                if minD[0] < start: minD.popleft()
                if maxD[0] < start: maxD.popleft()
            total_count += end - start + 1
            end += 1
        return total_count
