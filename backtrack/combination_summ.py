from typing import List
import bisect
import copy


class BestSolution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def dfs(cur, cur_sum, idx):  # try out each possible cases
            if cur_sum > target:
                return  # this is the case, cur_sum will never equal to target
            if cur_sum == target:
                ans.append(cur);
                return  # if equal, add to `ans`
            for i in range(idx, n):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i)  # DFS

        dfs([], 0, 0)
        return ans


class MySolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        _all_candidates = []

        def rec(arr):
            nonlocal results
            if sum(arr) > target:
                return
            elif sum(arr) == target:
                results.append(arr)
                return
            for candidate in candidates:
                bisect.insort(arr, candidate)
                _temp = copy.deepcopy(arr)
                if _temp not in _all_candidates:
                    _all_candidates.append(copy.deepcopy(_temp))
                    rec(_temp)
                arr.pop(arr.index(candidate))

        rec([])
        return results


class OptimizedSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def rec(arr, index):
            nonlocal results
            if sum(arr) > target:
                return
            elif sum(arr) == target:
                results.append(arr)
                return
            for index in range(index, len(candidates)):
                arr.append(candidates[index])
                _temp = copy.deepcopy(arr)
                rec(_temp, index)
                arr.pop()

        rec([], 0)
        return results


if __name__ == '__main__':
    BestSolution().combinationSum([2, 3, 6, 7], 7)
