class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        length = len(digits)
        index = length - 1
        
        while index >= 0:
            if digits[index] + carry == 10:
                digits[index] = 0
            else:
                digits[index] += carry
                return digits
            index -= 1

        result = [0] * (length + 1)
        result[0] = carry
        for position in range(length):
            result[position + 1] = digits[position]

        return result
