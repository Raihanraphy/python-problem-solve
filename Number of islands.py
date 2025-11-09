class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
      
        def dfs(row: int, col: int) -> None:
            
            
            grid[row][col] = '0'
          
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row, next_col = row + dr, col + dc
              
                
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    grid[next_row][next_col] == '1'):
                    
                    dfs(next_row, next_col)
      
        
        island_count = 0
      
        
        rows, cols = len(grid), len(grid[0])
      
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == '1':
                    
                    dfs(i, j)
                    
                    island_count += 1
      
        return island_count
