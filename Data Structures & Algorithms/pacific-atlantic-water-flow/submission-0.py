class Solution:


    def getNeighbors(self, row, col): 
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        neighbors = []
        for (dr, dc) in directions: 
            if 0 <= row+dr and row+dr < self.ROW and \
            0 <= col+dc and col+dc < self.COL:
                neighbors.append((row+dr, col + dc))
        
        return neighbors

    def dfs(self, r, c, ocean, visited): 
        if (r, c) in visited:
            return 
        visited.add((r,c)) 
        neighbors = self.getNeighbors(r, c)
        for (nr, nc) in neighbors: 
            if self.heights[r][c] <= self.heights[nr][nc]:
                ocean.add((nr, nc))
                self.dfs(nr, nc, ocean, visited)
 
    def findOcean(self, ocean):
        visited = set()
        for c in range(len(self.heights[0])):
            ocean.add((0, c))
            visited.clear()
            self.dfs(0, c, ocean, visited)
        for r in range(len(self.heights)):
            ocean.add((r, 0))
            visited.clear()
            self.dfs(r, 0, ocean, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        self.ROW = len(heights) 
        self.COL = len(heights[0])
        self.heights = heights

        pacific = set()
        self.findOcean(pacific)

        atlantic = set()
        visited = set()
        for c in range(len(self.heights[0])):
            atlantic.add((self.ROW-1, c))
            visited.clear()
            self.dfs(self.ROW-1, c, atlantic, visited)
        for r in range(len(self.heights)):
            atlantic.add((r, self.COL-1))
            visited.clear()
            self.dfs(r, self.COL-1, atlantic, visited)

        print("atl", sorted(atlantic))
        print("pacific", sorted(pacific))

        res = []
        for cell in pacific: 
            if cell in atlantic:
                res.append([cell[0], cell[1]])
        return res
        



        