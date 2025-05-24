class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize two variables that represent the base cases:
        # prev_step represents the number of ways to reach the step before the current one 
        # curr_step represents the number of ways to reach the current step. Initially set to 1 because there's 1 way to be at the first step.
        prev_step, curr_step = 0, 1
      
        # Loop for each step up to the nth step
        for _ in range(n):
            # At each step, the number of ways to reach the current step is the sum of the ways to reach the previous two steps.
            prev_step, curr_step = curr_step, prev_step + curr_step
      
        # After finishing the loop, curr_step contains the total number of ways to reach the nth step.
        return curr_step
