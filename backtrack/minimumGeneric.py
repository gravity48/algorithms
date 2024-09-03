from functools import reduce
from typing import List


class MySolution:
    """No result."""

    def backtrack(self, diffs, result, count):
        if not diffs:
            print(f'ok - count {count}')
            return True, count
        if result not in self.bank:
            return False, count
        results = []
        for elem_index, index in enumerate(diffs):
            res_ = f'{result[:index]}{self.endGene[index]}{result[index + 1:]}'
            new_diffs = diffs[:elem_index] + diffs[elem_index + 1:]
            status, count = self.backtrack(new_diffs, res_, count + 1)
            results.append((status, count))
        res = list(filter(lambda x: x[0], results))
        if not res:
            return False, 0
        else:
            res = reduce(lambda x, y: x if x[1] < y[1] else y, res)
            return res

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        self.bank = bank
        self.endGene = endGene
        diffs = []
        index = 0
        for start, end in zip(startGene, endGene):
            if start != end:
                diffs.append(index)
            index += 1
        results = []
        for index in diffs:
            res_ = f'{startGene[:index]}{endGene[index]}{startGene[index + 1:]}'
            status, count = self.backtrack(diffs, res_, 0)
            results.append((status, count))
        res = list(filter(lambda x: x[0], results))
        if not res:
            return -1
        _, min_count = reduce(lambda x, y: x if x[1] < y[1] else y, res)
        return min_count


from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # Create a set of all valid genes in the bank for faster access
        bankSet = set(bank)

        # Define the possible mutations for each character
        options = ['A', 'C', 'G', 'T']

        # Create a queue to store the genes to be checked
        queue = deque()
        queue.append(startGene)

        # Create a set to mark visited genes
        visited = set()
        visited.add(startGene)

        # Counter to keep track of the minimum mutations required to reach end gene
        count = 0

        # Perform BFS
        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j + 1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count += 1

        # If end gene not found
        return -1


if __name__ == '__main__':
    Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])
