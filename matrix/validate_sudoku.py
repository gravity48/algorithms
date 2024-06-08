from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_set_row = []
        board_set_col = []
        for _ in range(9):
            board_set_row.append(set())
            board_set_col.append(set())
        _squares = []
        for i in range(3):
            _squares.append([])
            for j in range(3):
                _squares[i].append(set())
        for i in range(9):
            for j in range(9):
                row_index = i // 3
                col_index = j // 3
                if board[i][j] == '.':
                        continue
                if board[i][j] in board_set_row[i]:
                    return False
                if board[i][j] in board_set_col[j]:
                    return False
                if board[i][j] in _squares[row_index][col_index]:
                    return False
                _squares[row_index][col_index].add(board[i][j])
                board_set_row[i].add(board[i][j])
                board_set_col[j].add(board[i][j])
        return True


if __name__ == '__main__':
    Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                              [".", "9", "8", ".", ".", ".", ".", "6", "."],
                              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                              [".", "6", ".", ".", ".", ".", "2", "8", "."],
                              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                              [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
