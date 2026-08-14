class Solution:
    # 30 min
    def getNeighbor(self, row, col):
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        res = []
        for d in dirs: 
            new_row = row + d[0]
            new_col = col + d[1]
            if 0 <= new_row and new_row < self.ROWS and \
            0 <= new_col and new_col < self.COLS: 
                res.append((new_row, new_col))
        return res

    def dfs(self, word, i, row, col, path):
        
        if (row, col) in path: 
            return False

        print("board[", row, "][", col, "]:", self.board[row][col], " word[i]", word[i])

        if i == len(word) - 1:
            if word[i] == self.board[row][col]: 
                path.add((row, col))
                return True
            return False
            
       
        if word[i] != self.board[row][col]:
            return False
        path.add((row, col))
        
        for d in self.getNeighbor(row, col):
            if self.dfs(word, i+1, d[0], d[1], path):
                return True
            
        path.remove((row, col))
        return False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.ROWS = len(board)
        self.COLS = len(board[0])

     
        for row in range(self.ROWS):
            for col in range(self.COLS):
                path = set()
                if self.dfs(word, 0, row, col, path):
                    return True
        return False

        