class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len (t):
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
        else:
            return False
        return True
