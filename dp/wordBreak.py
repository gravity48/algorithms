from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        alph = set()
        for word in wordDict:
            alph = alph | set(word)
        curr_alph = set(s)
        if not curr_alph.issubset(alph):
            return False
        wordDict = set(wordDict)
        visited = set()

        def rec(temp):
            if not temp:
                return True
            if temp in visited:
                return True
            res = ''
            results = []
            for index, letter in enumerate(temp):
                res += letter
                if res in wordDict:
                    visited.add(temp[:index + 1])
                    results.append(
                        rec(temp[index + 1:]),
                    )
            if not results:
                return False
            return any(results)

        return rec(s)


class RefactorSolution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if not wordDict or not s:
            return False
        max_length = 0
        for word in wordDict:
            max_length = max(max_length, len(word))
        wordDict = set(wordDict)
        results = [False] * (n + 1)
        results[0] = True
        for i in range(1, n + 1):
            roll_back = i - max_length - 1
            print(roll_back)
            for j in range(i - 1, max(i - max_length - 1, -1), -1):  # Only consider words that could fit
                print(f'J - {j} S - {s[j:i]} Max - {max(i - max_length - 1, -1)}')
                if results[j] and s[j:i] in wordDict:
                    results[i] = True
                    break

        return results[n]


if __name__ == '__main__':
    RefactorSolution().wordBreak('leetcode', ['leet', 'code', 'e', 'leete'])
