from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1] * (rowIndex + 1)
      
        for current_row in range(2, rowIndex + 1):

            for position in range(current_row - 1, 0, -1):

                row[position] += row[position - 1]
      
        return row
