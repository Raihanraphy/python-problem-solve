class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6
        
        base_case = {3: 3, 4: 4, 5: 6}
        n_3 = n // 3
        remainder = n % 3
        return 3 ** (n_3 - 1) * (base_case[3 + remainder])
