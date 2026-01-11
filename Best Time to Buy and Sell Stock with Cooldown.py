class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rest = 0
        hold = -float('inf')
        sold = -float('inf')

        for price in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_sold, prev_rest)
        
        return max(sold, rest)
