"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in range(length):
            for j in range(i, length):
                _tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = _tmp
        for i in range(length):
            matrix[i].reverse()


if __name__ == '__main__':
    Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
