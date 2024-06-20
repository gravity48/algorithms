from typing import List


class Solution:
    def binary_search(self, items: List[int], target: int):
        left, right = 0, len(items) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if items[mid] == target:
                return True, left
            elif items[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False, left - 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = [row[0] for row in matrix]
        status, index = self.binary_search(columns, target)
        if status:
            return True
        status, index = self.binary_search(matrix[index], target)
        return status


if __name__ == '__main__':
    Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
