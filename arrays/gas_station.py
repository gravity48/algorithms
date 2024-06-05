from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gas_tank, result = 0, 0
        for index in range(len(gas)):
            gas_tank += gas[index]
            gas_tank -= cost[index]
            if gas_tank < 0:
                result = index + 1
                gas_tank = 0
        return result


if __name__ == '__main__':
    Solution().canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])

