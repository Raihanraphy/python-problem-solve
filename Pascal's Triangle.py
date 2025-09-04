class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        if numRows == 0:
            return result

        result.append([1])  # First row

        for i in range(1, numRows):
            previous_row = result[i - 1]
            current_row = [1]  # First element is always 1

            for j in range(1, len(previous_row)):
                current_row.append(previous_row[j - 1] + previous_row[j])
            
            current_row.append(1)  # Last element is always 1
            result.append(current_row)

        return result
