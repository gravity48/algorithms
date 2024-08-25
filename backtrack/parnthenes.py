from typing import List


class BestSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return

            if openP < n:
                dfs(openP + 1, closeP, s + "(")

            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res


class MySolution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def rec(opened, closed, s):
            if len(s) == n * 2:
                result.append(s)
                return
            if opened < n:
                rec(opened + 1, closed, s + '(')
            rec(opened, closed + 1, s + ')')

        rec(0, 0, '')
        return result


if __name__ == '__main__':
    MySolution().generateParenthesis(2)
