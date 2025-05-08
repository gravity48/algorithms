class Solution:
    def isHappy(self, n: int) -> bool:
        items = set()
        while True:
            if n == 1:
                return True
            if n in items:
                return False
            items.add(n)
            temp = 0
            while n:
                ost = n % 10
                n = n // 10
                temp += (ost * ost)
            n = temp


if __name__ == '__main__':
    sol = Solution()
    sol.isHappy(7)
