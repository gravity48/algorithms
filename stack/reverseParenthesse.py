from collections import deque


class BestSolution:
    def reverseParentheses(self, s: str) -> str:
        ind_stack: deque[int] = deque()
        res: list[str] = []

        for char in s:
            if char == "(":  # start new string we need to reverse first
                ind_stack.append(len(res))  # string starts on next index
            elif char == ")":  # reverse string from last added start index
                start_ind: int = ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)

        return "".join(res)


class MySolution:

    def reverseParentheses(self, s: str) -> str:
        result_ = []
        arr_ = []
        for index, letter in enumerate(s):
            result_.append(letter)
            if letter == '(':
                arr_.append(index)
            if letter == ')':
                rev_index = arr_.pop()
                result_ = result_[:rev_index] + result_[rev_index:][::-1]
        return ''.join(filter(lambda x: x not in {'(', ')'}, result_))


if __name__ == '__main__':
    res = MySolution().reverseParentheses("(1(23)4)")
