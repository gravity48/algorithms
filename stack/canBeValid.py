class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        unlocked_stack = []
        opened_stack = []
        for index, letter in enumerate(s):
            if locked[index] == '0':
                unlocked_stack.append(index)
            elif letter == '(':
                opened_stack.append(index)
            elif letter == ')':
                if opened_stack:
                    opened_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
                else:
                    return False
        while opened_stack and unlocked_stack and opened_stack[-1] < unlocked_stack[-1]:
            opened_stack.pop()
            unlocked_stack.pop()
        if not opened_stack and unlocked_stack:
            return len(unlocked_stack) % 2 == 0
        return not opened_stack


if __name__ == '__main__':
    Solution().canBeValid('))()))', '010100')
