from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        if not coins:
            return 0
        results = [float('inf')] * (amount + 1)
        results[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                index = i - j
                if index < 0:
                    continue
                if results[index] < float('inf'):
                    results[i] = min(results[index] + 1, results[i])
        return results[-1] if results[-1] < float('inf') else -1


if __name__ == '__main__':
    Solution().coinChange([1, 2, 5], 11)
