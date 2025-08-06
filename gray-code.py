#gray-code
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        prev = self.grayCode(n-1)  # Get (n-1)-bit sequence
        add = 1 << (n-1)  # 2^(n-1) for prefixing
        return prev + [x + add for x in prev[::-1]]  # Append reversed with 1-prefix
