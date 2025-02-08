import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        conn = collections.defaultdict(list)
        for city_from, city_to in connections:
            conn[city_from].append((city_to, True))
            conn[city_to].append((city_from, False))
        nodes = [0]
        visited = {0}
        while nodes:
            node = nodes.pop()
            for child, cost in conn[node]:
                if child in visited:
                    continue
                visited.add(child)
                nodes.append(child)
                if cost:
                    ans += 1
        return ans

