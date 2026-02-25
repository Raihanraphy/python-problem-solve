class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return DP[1][n]

DP = [[inf for _ in range(201)] for _ in range(201)]

for sp in range(200, 0, -1):
    for ep in range(sp, 201):
        if ep == sp:
            DP[sp][ep] = 0
        else:
            for x in range(sp, ep + 1):
                if x == sp:
                    DP[sp][ep] = min(DP[sp][ep], x + DP[x + 1][ep])
                elif x == ep:
                    DP[sp][ep] = min(DP[sp][ep], x + DP[sp][x - 1])
                else:
                    DP[sp][ep] = min(DP[sp][ep], x + max(DP[sp][x - 1], DP[x + 1][ep]))
