class Solution:
    def rec(self, i, j, board, count, n):
        if board[i][j]:
            return 0
        start = i - n + 1
        end = j - n + 1
        for index in range(n):
            board[i][index] = 1
            board[index][j] = 1
            if start + index > -1 and end + index > -1:
                board[start][end] = 1
        count -= 1
        if count == 0:
            return 1
        result = 0
        for x in range(n):
            for y in range(n):
                board = copy.deepcopy(board)
                if not board[x][y]:
                    result += self.rec(x, y, board, count, n)
        return result

    def totalNQueens(self, n: int) -> int:
        for i in range(n):
            for j in range(n):
                board = [[0] * n for i in range(n)]
                res = self.rec(i, j, board, n, n)
        return res