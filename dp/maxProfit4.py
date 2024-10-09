from typing import List
import heapq


class MySolution:

    def mergeIntervals(self, dp: list):
        if not dp:
            return []
        dp.sort(key=lambda x: x[0])
        result = []
        start, end = dp[0]
        for _start, _end in dp[1:]:
            if end >= _start:
                end = _end
            else:
                heapq.heappush(result, start - end)
                start = _start
                end = _end
        heapq.heappush(result, start - end)
        return result

    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = []
        minimum = prices[0]
        prev = prices[0]
        is_buy = False
        for price in prices[1:]:
            if is_buy is False and price < prev:
                ...
            elif is_buy is False and price > prev:
                minimum = prev
                is_buy = True
            elif is_buy and price > prev:
                ...
            elif is_buy and price < prev:
                is_buy = False
                dp.append([minimum, prev])
            prev = price
        if is_buy:
            dp.append([minimum, prev])
        dp = self.mergeIntervals(dp)
        result = 0
        while k and len(dp):
            result -= heapq.heappop(dp)
            k -= 1
        return result


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # T.C.: O(N*k) S.C.: O(k)

        n = len(prices)

        if n == 0 or k == 0:
            return 0

        buyPrice = [float('inf')] * k
        profit = [float('-inf')] * k

        for price in prices:

            # Loop is needed for dealing with k transactions.

            for i in range(k):
                # Update buy[i] and profit[i] for each transaction

                buyPrice[i] = min(buyPrice[i], price - (profit[i - 1] if i > 0 else 0))
                profit[i] = max(profit[i], price - buyPrice[i])

        return profit[k - 1]


if __name__ == '__main__':
    Solution().maxProfit(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
