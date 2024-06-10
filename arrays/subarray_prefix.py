from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        d = {0: 1}

        index = 0
        prefix_sum = 0
        for item in nums:
            prefix_sum = prefix_sum + item

            if prefix_sum - k in d:
                result += d[prefix_sum - k]
            index += 1
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
        return result


if __name__ == '__main__':
    Solution().subarraySum([1,-1, 0], 0)
