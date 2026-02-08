def reverseString(s: list[str]) -> None:
    """
    Reverses a string (list of characters) in-place using O(1) extra memory.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1

# Example 1 Usage:
s1 = ["h","e","l","l","o"]
reverseString(s1)
print(f"Example 1 Output: {s1}") # Output: ['o', 'l', 'l', 'e', 'h']

# Example 2 Usage:
s2 = ["H","a","n","n","a","h"]
reverseString(s2)
print(f"Example 2 Output: {s2}") # Output: ['h', 'a', 'n', 'n', 'a', 'H']
