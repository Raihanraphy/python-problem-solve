class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [char for char in s.lower() if char.isalnum()]
        return word == list(reversed(word))
