class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n = n // 4

        if n % 8 == 7:
            return 4

        rt = int(sqrt(n))
        if rt * rt == n:
            return 1

        for i in range(1, rt + 1):
            rt1 = int(sqrt(n - i * i))
            if rt1 * rt1 == n - i * i:
                return 2

        return 3
