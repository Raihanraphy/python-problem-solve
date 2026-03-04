class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
            
        return True

