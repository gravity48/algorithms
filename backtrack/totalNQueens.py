class Solution:

    def totalNQueen(self, n: int):
        state = [['.'] * n for _ in range(n)]
        visited_cols = set()
        visited_antidiag = set()
        visited_diag = set()
        res = set()

        def backtrack(r):
            if r == n:
                res.add(''.join(map(''.join, state)))
                return
            for c in range(n):
                if not (c in visited_cols or (r - c) in visited_diag or (r + c) in visited_antidiag):
                    visited_cols.add(c)
                    visited_diag.add(r - c)
                    visited_antidiag.add(r + c)
                    state[r][c] = 'Q'
                    backtrack(r + 1)

                    visited_cols.remove(c)
                    visited_diag.remove(r - c)
                    visited_antidiag.remove(r + c)
                    state[r][c] = '.'

        backtrack(0)
        return len(res)


class MySolution:
    def totalNQueens(self, n: int) -> int:
        visited_cols = set()
        visited_diag = set()
        visited_antidiag = set()
        result = 0

        def backtracking(r):
            nonlocal result
            if r == n:
                result += 1
                return
            for c in range(n):
                if not(c in visited_cols or (r + c) in visited_antidiag or (r - c) in visited_diag):
                    visited_cols.add(c)
                    visited_diag.add(r - c)
                    visited_antidiag.add(r + c)

                    backtracking(r + 1)
                    visited_cols.remove(c)
                    visited_diag.remove(r - c)
                    visited_antidiag.remove(r + c)
        backtracking(0)
        return result


if __name__ == '__main__':
    Solution().totalNQueen(4)
