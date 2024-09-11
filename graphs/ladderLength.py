from collections import defaultdict
from collections import deque
from typing import List


class MySolution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        visited = {beginWord}
        count = 1
        while queue:
            temp = []
            for word in queue:
                if word == endWord:
                    return count
                for bank in wordList:
                    diff = 0
                    for letter1, letter2 in zip(word, bank):
                        if letter1 != letter2:
                            diff += 1
                        if diff == 2:
                            break
                    if diff == 1 and bank not in visited:
                        temp.append(bank)
                        visited.add(bank)
            queue = temp
            count += 1
        return 0


class BestSolution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        # Обратить внимание на хеш таблицу
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0


if __name__ == '__main__':
    BestSolution().ladderLength('hit', 'cog',
                                ["hot", "dot", "dog", "lot", "log", "cog"])
