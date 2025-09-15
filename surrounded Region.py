class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x,y):
            if m<=x or x<0 or n<=y or y<0 or board[x][y]!="O":
                    return 
            board[x][y]="E"
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(x+dx,y+dy)

        
        m=len(board)
        n=len(board[0])
    
        for i in range(m):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][n-1]=="O":
                dfs(i,n-1)
        for j in range(n):
            if board[0][j]=="O":
                dfs(0,j)
            if board[m-1][j]=="O":
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="E":
                    board[i][j]="O"
        return board
