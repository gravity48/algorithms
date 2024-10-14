from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Ошибка того что надо было решать не сначала как я начал а с конца.
        """
        nums3 = []
        index1 = 0
        index2 = 0
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return

        while True:
            if index1 == m:
                nums3 += nums2[index2: n]
                break
            if index2 == n:
                nums3 += nums1[index1: m]
                break
            if nums1[index1] < nums2[index2]:
                nums3.append(nums1[index1])
                index1 += 1
            else:
                nums3.append(nums2[index2])
                index2 += 1
        nums1[:] = nums3


class BestSolution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


class NewSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        local_index = m + n - 1
        while index1 > -1 or index2 > -1:
            if index1 > -1 and index2 > -1 and nums1[index1] >= nums2[index2]:
                nums1[local_index] = nums1[index1]
                index1 -= 1
            elif index1 > -1 and index2 > -1 and nums1[index1] < nums2[index2]:
                nums1[local_index] = nums2[index2]
                index2 -= 1
            elif index2 == 0:
                return
            else:
                nums1[local_index] = nums2[index2]
                index2 -= 1
            local_index -= 1


if __name__ == '__main__':
    NewSolution().merge([0], 0, [1], 1)


class TestSolution:

    def test_01(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        NewSolution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_02(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1]

    def test_03(self):
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == [1, 2]
