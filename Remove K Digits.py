class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # If we have to remove all digits, return immediately.
        if len(num) == k: 
            return "0"
            
        stack = []
        
        for digit in num:
            # While we still have removals left, the stack isn't empty, 
            # and the current digit is smaller than the top of the stack:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If we went through the whole string but still have removals left 
        # (e.g., the string was strictly increasing like "12345")
        if k > 0:
            stack = stack[:-k]
            
        # Join the stack into a string and strip leading zeros safely.
        res = "".join(stack).lstrip('0')
        
        # If stripping zeros leaves an empty string, return "0"
        return res if res else "0"
