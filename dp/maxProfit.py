from typing import List


class MySolution:

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [0] * length
        index = 1
        minimum = prices[0]
        for price in prices[1:]:
            delta = price - minimum
            minimum = min(minimum, price)
            dp[index] = max(dp[index - 1], delta)
            index += 1
        result = 0
        for index0 in range(1, length):
            for index1 in range(max(index0 - 1, -1), -1, -1):
                delta = prices[index0] - prices[index1]
                result = max(result, delta + dp[index1])
        return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # initialize variables for first buy, first sell, second buy, and second sell
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        # iterate over prices to update buy and sell values
        for price in prices:
            # update first buy and sell values
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # update second buy and sell values
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2


if __name__ == '__main__':
    Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
