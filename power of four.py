class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & (n-1) == 0 and n % 3 == 1:
            return True
        return False
