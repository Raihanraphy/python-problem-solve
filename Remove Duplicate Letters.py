class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        stack = []
        in_stack = set()

        for c in s:
            count[c] -= 1

            if c in in_stack:
                continue

            while stack and stack[-1] > c and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(c)
            in_stack.add(c)

        return "".join(stack)
            
            
        
