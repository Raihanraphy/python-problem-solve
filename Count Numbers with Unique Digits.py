class Solution:
    def solve(self, s, i, tight, mask, leading_zero, dp):
        if i == len(s):
            return 1  # valid number formed

        key = (i, tight, mask, leading_zero)
        if key in dp:
            return dp[key]

        limit = int(s[i]) if tight else 9
        res = 0

        for d in range(limit + 1):
            ntight = tight and (d == limit)

            if leading_zero and d == 0:
                # still leading zero, mask unchanged
                res += self.solve(s, i + 1, ntight, mask, True, dp)
            else:
                # check if digit already used
                if (mask & (1 << d)) != 0:
                    continue
                res += self.solve(
                    s,
                    i + 1,
                    ntight,
                    mask | (1 << d),
                    False,
                    dp
                )

        dp[key] = res
        return res

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        s = str(10**n - 1)
        dp = {}
        return self.solve(s, 0, True, 0, True, dp)
