class Solution:
    def reverse(self, x: int) -> int:
        r = int(str(abs(x))[::-1])
        if x < 0: r *= -1
        return r if -2**31 < r < 2**31-1 else 0