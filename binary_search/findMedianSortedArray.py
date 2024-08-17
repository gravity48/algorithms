from typing import List


class MySolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        length1 = len(nums1)
        length2 = len(nums2)
        total_length = length1 + length2
        mid = total_length // 2 + 1
        prev = None
        index1 = 0
        index2 = 0
        value = 0
        while mid:
            prev = value
            if index1 > length1 - 1:
                value = nums2[index2]
                # print(f'Value num2 if not exists num1 {value}')
                index2 += 1
            elif index2 > length2 - 1:
                value = nums1[index1]
                # print(f'Value num1 if not exists num2 {value}')
                index1 += 1
            elif nums1[index1] < nums2[index2]:
                value = nums1[index1]
                # print(f'Value num1 {value}')
                index1 += 1
            else:
                value = nums2[index2]
                # print(f'Value num2 {value}')
                index2 += 1
            mid -= 1
        # print(f'Value {value} Prev - {prev}')
        return prev + (value - prev) / 2 if not total_length % 2 else value


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        left = (n1 + n2 + 1) // 2  # Calculate the left partition size
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2  # Calculate mid index for nums1
            mid2 = left - mid1  # Calculate mid index for nums2

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            # Determine values of l1, l2, r1, and r2
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1

        return 0  # If the code reaches here, the input arrays were not sorted.


if __name__ == '__main__':
    Solution().findMedianSortedArrays([2, 3, 4], [1, 5, 6, 7])
