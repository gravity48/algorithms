from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr = 0
        max_sum = float('-inf')
        flag = 1
        ans = float('-inf')
        # check if all elements are negative
        for i in nums:
            if i >= 0:
                flag = 0
                break
            ans = max(ans, i)
        # if all elements are negative return the largest one
        if flag:
            return ans
        # find max subarray sum using kadane's algorithm
        for i in nums:
            total_sum += i
            curr += i
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        min_sum = float('inf')
        curr = 0
        # find min subarray sum
        for i in nums:
            curr += i
            min_sum = min(min_sum, curr)
            if curr > 0:
                curr = 0
        # find the maximum sum of subarray by comparing the max subarray sum and total sum - min subarray sum
        ans2 = total_sum - min_sum
        return max(max_sum, ans2)


class MySolution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        flag = True
        for num in nums:
            if num >= 0:
                flag = False
        if flag:
            return max(nums)
        local_sum = nums[0]
        global_sum = nums[0]
        local_min = nums[0]
        global_min = nums[0]
        total_sum = nums[0]
        for num in nums[1:]:
            total_sum += num
            local_sum = max(num, local_sum + num)
            local_min = min(num, local_min + num)
            global_sum = max(local_sum, global_sum)
            global_min = min(local_min, global_min)
        return max(global_sum, total_sum - global_min)


if __name__ == '__main__':
    MySolution().maxSubarraySumCircular([5, -3, 5])
