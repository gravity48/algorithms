from collections import deque
from typing import List


class MySolution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = 0
        for row in range(rows):
            if row - 1 > -1:
                for col in range(cols):
                    dp[row][col] = min(
                        dp[row][col],
                        dp[row - 1][col] if grid[row - 1][col] == 3 else dp[row - 1][col] + 1)
            for col in range(1, cols):
                dp[row][col] = min(
                    dp[row][col],
                    dp[row][col - 1] if grid[row][col - 1] == 1 else dp[row][col - 1] + 1)
            for col in range(cols - 2, -1, -1):
                dp[row][col] = min(
                    dp[row][col],
                    dp[row][col + 1] if grid[row][col + 1] == 2 else dp[row][col + 1] + 1)
        return dp[rows - 1][cols - 1]


class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0
        dque = deque([(0, 0)])

        while dque:
            x, y = dque.popleft()

            for index, (vertical, horizontal) in enumerate(directions):
                if (
                    -1 < x + vertical < rows
                    and -1 < y + horizontal < cols
                ):
                    cost = 0 if (index + 1) == grid[x][y] else 1
                    if dp[x + vertical][y + horizontal] > dp[x][y] + cost:
                        dp[x + vertical][y + horizontal] = dp[x][y] + cost
                        dque.append((x + vertical, y + horizontal))
        return dp[rows - 1][cols - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 3, 3],
        [2, 2, 1, 2],
        [4, 3, 3, 4],
        [3, 2, 2, 3],
        [3, 2, 1, 3],
        [4, 1, 4, 3],
        [3, 3, 1, 2],
    ]
    answer = MySolution().minCost(grid)
    answer2 = Solution().minCost(grid)
    print(answer2, answer)
