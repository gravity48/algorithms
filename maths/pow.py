class Solution:
    def helper(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.helper(x *x, n // 2)
        else:
            return x * self.helper(x * x, (n - 1) // 2)

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n)
        return 1 / self.helper(x, -n)
