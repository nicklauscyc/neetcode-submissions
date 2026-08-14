class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # first solve in O(n) space
        R = len(matrix)
        C = len(matrix[0])
        zeros = []
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    for row in range(R):
                        zeros.append((row, c))
                    for col in range(C):
                        zeros.append((r, col))
        
        for (r, c) in zeros:
            matrix[r][c] = 0
        
        
        