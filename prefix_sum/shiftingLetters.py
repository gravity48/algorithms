from typing import List
from itertools import accumulate


class MySolution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_array = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            prefix_array[start] += 1 if direction else -1
            prefix_array[end + 1] += -1 if direction else 1
        temp = list(accumulate(prefix_array))
        prefix_array = temp
        result = ''
        for index, letter in enumerate(s):
            shift = prefix_array[index] % 26
            letter_num = ord(letter) + shift
            if 97 <= letter_num <= 122:
                result += chr(letter_num)
            elif letter_num < 97:
                result += chr(123 - (97 - letter_num))
            else:
                result += chr(96 + (letter_num - 122))
        return result


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)

        for shiftOp in shifts:
            start, end, direction = shiftOp
            shift[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if direction == 1 else -1)

        currentShift = 0
        shiftList = list(s)
        for i in range(n):
            currentShift += shift[i]
            netShift = (currentShift % 26 + 26) % 26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shiftList)


if __name__ == '__main__':
    Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]])
