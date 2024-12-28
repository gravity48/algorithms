from typing import List


class Solution:

    def binarySearch(self, spell, success):
        l = 0
        r = len(self.potions) - 1
        while l <= r:
            m = l + (r - l) // 2
            if (self.potions[m] * spell) >= success:
                r = m - 1
            else:
                l = m + 1
        return len(self.potions) - l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        self.potions = potions
        result = []
        for spell in spells:
            result.append(self.binarySearch(spell, success))
        return result


if __name__ == '__main__':
    Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)
