from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        col_length = len(matrix[0])
        row_length = len(matrix)
        matrix_size = col_length * row_length
        row = 0
        col = 0
        while len(result) != matrix_size:
            for j in range(col, col_length):
                result.append(matrix[row][j])
            for i in range(row + 1, row_length):
                result.append(matrix[i][col_length - 1])
            if row_length != row + 1:
                for j in range(col_length - 2, col - 1, -1):
                    result.append(matrix[row_length - 1][j])
            if col_length != col+1:
                for i in range(row_length - 2, row, -1):
                    result.append(matrix[i][col])
            row += 1
            col += 1
            col_length -= 1
            row_length -= 1
        return result

if __name__ == '__main__':
    Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

