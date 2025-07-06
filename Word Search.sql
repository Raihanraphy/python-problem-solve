python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
        def dfs (char_index,row,col) :
            if char_index == len(word) : return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) :
                return False
            if board[row][col] == "#" or board[row][col] != word[char_index] : return False
            value = board[row][col]
            board[row][col] = "#"
            result = (
                dfs(char_index+1,row + 1,col) or 
                dfs(char_index+1,row,col + 1) or 
                dfs(char_index+1,row - 1 , col) or 
                dfs(char_index+1,row,col-1)
            ) 
            board[row][col] = value    
            return result                
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if word[0] == board[i][j] :
                    if dfs(0,i,j) :
                        return True
        return False    
