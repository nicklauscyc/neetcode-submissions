class Solution:
    # 19 mins
    def getNeighbors(self, row, col): 
        maxRow = self.maxRow
        maxCol = self.maxCol
        n = []
        # up down left right
        if 0 <= row - 1 and row - 1 < maxRow:
            n.append((row - 1, col))

        if 0 <= row + 1 and row + 1 < maxRow:
            n.append((row + 1, col))

        if 0 <= col - 1 and col - 1 < maxCol:
            n.append((row, col - 1))

        if 0 <= col + 1 and col + 1 < maxCol:
            n.append((row, col + 1))
        return n
    
    def dfs(self, row, col, visited, tree):
        if (row, col) in visited:
            return 
        visited.add((row, col))
        if self.grid[row][col] == "1":
            tree.add((row, col))
        else:
            return # Water, I cannot travel

        for n in self.getNeighbors(row, col):
            self.dfs(n[0], n[1], visited, tree)

    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs through the grid on 1s and for each dfs tree create a set 
        # count the number of trees at the end through sets.
        self.maxRow = len(grid)
        self.maxCol = len(grid[0])
        self.grid = grid
        visited = set()
        trees = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited:
                    continue
                tree = set()
                self.dfs(row, col, visited, tree)
                if tree:
                    trees += 1
        return trees

                

        