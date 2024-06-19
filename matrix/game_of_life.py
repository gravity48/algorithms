from typing import List

class Solution:
    def getNeightBours(self, i, j):
        _sum = 0
        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                if i == row and col == j:
                    continue
                if i < 0 or i > self.m - 1:
                    continue
                if j < 0 or j > self.n - 1:
                    continue
                _sum += self._board[i][j]
        return _sum

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self._board = board
        changed = []
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                _cell = board[i][j]
                _sum = self.getNeightBours(i, j)
                if _sum < 2 and _cell:
                    changed.append((i, j))
                    continue
                if (_sum == 2 or _sum == 3) and _cell:
                    continue
                if _sum > 3 and _cell:
                    changed.append((i, j))
                    continue
                if _sum == 3 and not _cell:
                    changed.append((i, j))
                    continue
        for i, j in changed:
            if board[i][j]:
                board[i][j] = 0
            else:
                board[i][j] = 1

if __name__ == '__main__':
    Solution().gameOfLife([[0]])