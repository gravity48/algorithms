class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp = ''
        num = 0
        for letter in s:
            if letter.isdigit():
                num *= 10
                num += int(letter)
            elif letter == '[':
                stack.append((tmp, num))
                tmp = ''
                num = 0
            elif letter == ']':
                last_string, number = stack.pop()
                tmp = last_string + number * tmp
            else:
                tmp += letter

        return tmp


if __name__ == '__main__':
    Solution().decodeString("3[a]2[bc]")
