"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a
non-empty word in s.
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        verify_array = s.split(' ')
        if len(verify_array) != len(pattern):
            return False
        _map = {}
        _set = set()
        for index, letter in enumerate(pattern):
            if letter not in _map and letter not in _set:
                _map[letter] = verify_array[index]
                _set.add(letter)
            if letter not in _map and letter in _set:
                return False
            if _map[letter] != verify_array[index]:
                return False
        return True


if __name__ == '__main__':
    Solution().wordPattern('abba', 'dog dog dog dog')
