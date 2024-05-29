"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        start = 0
        end = 0
        substr_ = ''
        for index in haystack:
            substr_ += index
            end += 1
            if substr_ == needle:
                return start
            while needle.find(substr_) != 0:
                substr_ = substr_[1:]
                start += 1
        return -1


if __name__ == '__main__':
    Solution().strStr('hello', 'll')