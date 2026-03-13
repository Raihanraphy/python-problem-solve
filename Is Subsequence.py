class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(t):
            if j < len(s) and t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
            i += 1
        
        return True if len(t) == 0 else False
