from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                results.append(l + r)
                            elif ch == "-":
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)

            # base case: expr is a number
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return compute(expression)
