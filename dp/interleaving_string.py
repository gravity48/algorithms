class MySolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [(0, 0)]
        for letter in s3:
            temp = set()
            for tmp1, tmp2 in dp:
                if tmp1 < len(s1) and s1[tmp1] == letter:
                    temp.add((tmp1 + 1, tmp2))
                if tmp2 < len(s2) and s2[tmp2] == letter:
                    temp.add((tmp1, tmp2 + 1))
            if not temp:
                return False
            dp = list(temp)
        else:
            return True


class BestSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[m][n]
