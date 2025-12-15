class Solution:
    def gameOfLife(self, board: List[List[int]]):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        new_board = [[0] * cols for _ in range(rows)]

        dirs = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (1, -1),
            (-1, 1), (-1, -1)
        ]

        for r in range(rows):
            for c in range(cols):
                live_neig = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols):
                        continue
                    if board[nr][nc] == 1:
                        live_neig += 1
                if board[r][c] == 0:
                    if live_neig == 3:
                        new_board[r][c] = 1
                else:
                    if live_neig >= 2 and live_neig <= 3:
                        new_board[r][c] = 1
                    else:
                        new_board[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                board[r][c] = new_board[r][c]
