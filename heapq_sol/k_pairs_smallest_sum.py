from typing import List
import heapq


class MySolution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        length = len(nums2)
        for index, value in enumerate(nums1):
            heapq.heappush(heap, (value + nums2[0], (index, 0)))
        while k and heap:
            value, (index1, index2) = heapq.heappop(heap)
            result.append([nums1[index1], nums2[index2]])
            if index2 + 1 < length:
                heapq.heappush(heap, (nums1[index1] + nums2[index2 + 1], (index1, index2 + 1)))
            k -= 1
        return result


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        resV = []  # Result list to store the pairs
        pq = []  # Priority queue to store pairs with smallest sums, sorted by the sum

        # Push the initial pairs into the priority queue
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0],
                                0])  # The sum and the index of the second element in nums2

        # Pop the k smallest pairs from the priority queue
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[
                1]  # Get the smallest sum and the index of the second element in nums2

            resV.append([s - nums2[pos], nums2[pos]])  # Add the pair to the result list

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  # Decrement k

        return resV  # Return the k smallest pairs


if __name__ == '__main__':
    Solution().kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 20)
