from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitals = {}
        for index, cost in enumerate(capital):
            _set = capitals.get(cost, set())
            _set.add((profits[index], index, cost))
            capitals[cost] = _set
        for _ in range(k):
            _max_profit_res = -1
            proj_index_res = -1
            cost_res = -1
            for i in range(w + 1):
                current_projects = capitals.get(i) or {(-1, -1, -1)}
                _max_profit, projects_index, cost = max(list(current_projects),
                                                        key=lambda x: x[0])
                if _max_profit > _max_profit_res:
                    _max_profit_res, proj_index_res, cost_res = _max_profit, projects_index, cost
            if _max_profit_res == -1:
                break
            w += _max_profit_res
            capitals[cost_res].remove((_max_profit_res, proj_index_res, cost_res))
        return w


class BestSolution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)

        return w


if __name__ == '__main__':
    BestSolution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
