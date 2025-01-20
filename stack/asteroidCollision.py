from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            while (
                stack
                and item < 0
                and stack[-1] > 0
            ):
                if -item > stack[-1]:
                    stack.pop()
                    continue
                elif -item == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(item)
        return stack


if __name__ == '__main__':
    Solution().asteroidCollision([-2, -2, 1, -2])
