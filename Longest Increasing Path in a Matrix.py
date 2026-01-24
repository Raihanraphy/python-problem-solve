class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from functools import cache
      
        @cache
        def dfs(row: int, col: int) -> int:
    
            # Initialize the maximum path length from neighboring cells
            max_path_length = 0
          
            # Check all four directions: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
          
            for delta_row, delta_col in directions:
                # Calculate neighboring cell coordinates
                next_row = row + delta_row
                next_col = col + delta_col
              
                # Check if the neighbor is within bounds and has a greater value
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    matrix[next_row][next_col] > matrix[row][col]):
                    # Recursively find the longest path from the neighbor
                    max_path_length = max(max_path_length, dfs(next_row, next_col))
          
            # Return the longest path including the current cell (+1)
            return max_path_length + 1
      
        # Get matrix dimensions
        rows = len(matrix)
        cols = len(matrix[0])
      
        # Find the maximum path length starting from each cell
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i, j))
      
        return max_path
