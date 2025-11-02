class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        profits, v_stack, p_stack = [], [], []

        i, n = 0, len(prices)
        while i < n:
            v = i
            while v + 1 < n and prices[v + 1] <= prices[v]:
                v += 1
            
            p = v
            while p + 1 < n and prices[p + 1] >= prices[p]:
                p += 1
            
            while v_stack and prices[v] <= prices[v_stack[-1]]:
                profits.append(-(prices[p_stack.pop()] - prices[v_stack.pop()]))

            while p_stack and prices[p] >= prices[p_stack[-1]]:
                profits.append(-(prices[p_stack[-1]] - prices[v]))
                v = v_stack.pop()
                p_stack.pop()

            v_stack.append(v)
            p_stack.append(p)
            i = p + 1
        
        while v_stack:
            profits.append(-(prices[p_stack.pop()] - prices[v_stack.pop()]))

        heapq.heapify(profits)
        return sum(-heapq.heappop(profits) for _ in range(min(k, len(profits))))
