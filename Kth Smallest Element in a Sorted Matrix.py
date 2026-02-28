class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start = matrix[0][0]
        end = matrix[n - 1][n - 1]
        def countLessEqual(mid):
            row = n - 1
            col = 0 
            count = 0
            while row >= 0 and col < n:
                if mid >= matrix[row][col]: 
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count
        while start < end:
            mid = (start + end) // 2
            if countLessEqual(mid) < k:
                start = mid + 1
            else:
                end = mid 
        
        return start
