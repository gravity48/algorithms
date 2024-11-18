class Solution:
    def binarySearch(self, arr, target):
        """binary search."""
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l, r


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 7, 8, 9]

    print(Solution().binarySearch([1, 2, 3, 4, 7, 8, 9], 5))
    print(Solution().binarySearch([1, 2, 3, 4, 7, 8],3 ))
