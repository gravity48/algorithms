from typing import List


class Solution:
    def formatting_buff(self, buff, maxWidth, is_last):
        if len(buff) == 1:
            spaces = ' ' * (maxWidth - len(' '.join(buff)))
            buff.append(spaces)
            return ''.join(buff)
        if is_last:
            num_of_letters = len(''.join(buff))
            return ' '.join(buff) + ' '*(maxWidth - num_of_letters - len(buff) + 1)
        num_spaces = (maxWidth - len(''.join(buff)))
        spaces_len, num_extra_spaces  = divmod(num_spaces, (len(buff) - 1))
        for i in range(num_extra_spaces):
            buff[i] += ' '
        spaces = ' ' * spaces_len
        output = buff[0]
        index = 1
        while index < len(buff):
            output += f'{spaces}{buff[index]}'
            index += 1
        return output

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buff = []
        output = []
        for word in words:
            buff.append(word)
            length = len(' '.join(buff))
            if length > maxWidth:
                buff.pop()
                output.append(self.formatting_buff(buff, maxWidth, False))
                buff.clear()
                buff.append(word)
        if buff:
            output.append(self.formatting_buff(buff, maxWidth, True))
        return output


if __name__ == '__main__':
    Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)

