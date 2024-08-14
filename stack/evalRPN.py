from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        if len(tokens) < 2:
            return int(tokens[0])
        arr = []
        maths = {'+', '-', '/', '*'}
        for token in tokens:
            if token not in maths:
                arr.append(int(token))
            else:
                num2 = arr.pop()
                num1 = arr.pop()
                if token == '+':
                    arr.append(num1 + num2)
                elif token == '-':
                    arr.append(num1 - num2)
                elif token == '*':
                    arr.append(num1 * num2)
                else:
                    arr.append(int(num1 / num2))
        return arr[-1]


if __name__ == '__main__':
    Solution().evalRPN(["4", "-2", "/", "2", "-3", "-", "-"])
