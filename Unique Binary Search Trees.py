class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 0 nodes, 1 empty tree
        
        for i in range(1, n + 1):  # Iterate for number of nodes from 1 to n
            for j in range(i):  # Iterate for possible root positions (0 to i-1 for left subtree size)
                dp[i] += dp[j] * dp[i - 1 - j]
        
        return dp[n]
