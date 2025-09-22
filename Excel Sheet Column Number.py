class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Calculate the numerical value of the character (A=1, B=2, ..., Z=26)
            char_value = ord(char) - ord('A') + 1
            # Update the result using base-26 logic
            result = result * 26 + char_value
        return result
